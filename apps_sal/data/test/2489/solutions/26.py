N = int(input())
a = list(map(int, input().split()))
cnt = {}
for item in a:
    if item not in cnt:
        cnt[item] = 0
    cnt[item] += 1
A = list(set(a))
candidate = []
for item in A:
    if cnt[item] == 1:
        candidate.append(item)
judge = [True] * (10 ** 6 + 1)
for item in A:
    for i in range(2, 10 ** 6 // item + 1):
        judge[item * i] = False
ans = 0
for item in candidate:
    if judge[item]:
        ans += 1
print(ans)

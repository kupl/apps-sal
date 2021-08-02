n, k = map(int, input().split())
cnt = [1] * n
for i in range(k):
    d = int(input())
    a = [*map(int, input().split())]
    for j in a:
        cnt[j - 1] = 0

ans = 0
for i in cnt:
    if i == 1:
        ans += 1
print(ans)

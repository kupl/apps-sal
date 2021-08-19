N = int(input())
A = list(map(int, input().split()))
A.sort()
MAX = 10 ** 6 + 1
cnt = [0] * MAX
for x in A:
    if cnt[x] != 0:
        cnt[x] = 2
    else:
        for i in range(x, MAX, x):
            cnt[i] += 1
ans = 0
for x in A:
    if cnt[x] == 1:
        ans += 1
print(ans)

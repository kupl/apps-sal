from bisect import bisect_left

N, K = [int(x) for x in input().split()]
a = [0] + [int(x) for x in input().split()]
s = [0]*(N + 1)
for i in range(1, N + 1):
    s[i] = s[i - 1] + a[i]

ans = 0
for i in range(1, N + 1):
    j = bisect_left(s, K + s[i - 1])
    ans = ans + N - j + 1

print(ans)

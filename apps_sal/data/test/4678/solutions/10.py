# -*- coding utf-8 -*-

MOD = 10 ** 9 + 7

N = int(input())
AN = list(map(int, input().split()))

ans = 0
m = AN[0]
for i in range(1, N):
    if m > AN[i]:
        ans += m - AN[i]
    m = max(m, AN[i])

print(ans)


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

N, K = map(int, input().split())

lst = [0] * (K + 1)

for i in range(K, 0, -1):
    a = K // i
    tmp = pow(a, N, MOD)
    for j in range(i + i, K + 1, i):
        tmp -= lst[j]
    lst[i] = tmp

ans = 0
for i in range(K + 1):
    ans += i * lst[i]
    ans %= MOD

print(ans)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

K = int(input())
N = 50

tmp1 = N - 1 + (K // N)
tmp2 = K % 50

ans = [0] * N
for i in range(N - tmp2):
    ans[i] = tmp1 - tmp2
for j in range(i + 1, N):
    ans[j] = tmp1 + N - tmp2 + 1

print(N)
print(*ans, sep=' ')

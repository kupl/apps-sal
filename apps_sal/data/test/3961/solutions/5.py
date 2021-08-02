import sys
MOD = 10 ** 9 + 7
N = int(input())
bs = [int(b) - 1 for b in input().split()]
fs = [0]
for i in range(1, N + 1):
    f = 2 * fs[i - 1] + 2 - fs[bs[i - 1]]
    fs.append(f % MOD)
print(fs[-1])

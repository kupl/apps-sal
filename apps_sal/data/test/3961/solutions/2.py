import sys
MOD = 10**9 + 7
N = int(sys.stdin.readline())
bs = [int(b) - 1 for b in sys.stdin.readline().split()]
fs = [0]
for i in range(1, N + 1):
    f = 2 * fs[i - 1] + 2 - fs[bs[i - 1]]
    fs.append(f % MOD)
print(fs[-1])

import sys
read = lambda: list(map(int, sys.stdin.readline().split()))
n, = read()
a0s = read()
a1s = read()
bs = read()
best = 10**8
for i in range(n):
    for j in range(i + 1, n):
        res = sum(a0s[:i]) + sum(a0s[:j]) \
            + bs[i] + bs[j] \
            + sum(a1s[i:]) + sum(a1s[j:])
        #print(i, j, res)
        if res < best:
            best = res

print(best)

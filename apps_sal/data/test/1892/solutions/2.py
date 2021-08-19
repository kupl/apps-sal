import sys
sys.setrecursionlimit(1000000)
read = sys.stdin.readline

MOD = 1000000007

N = int(read())
sts = [read().strip() for _ in range(N)]

ind = [0 for _ in range(N)]
ind[0] = 1
indent = 0
last = 'f'
for st in sts:
    if last != 'f':
        for i in range(indent, -1, -1):
            ind[i] += ind[i + 1]
            ind[i] %= MOD
    if st == 'f':
        indent += 1
        for i in range(indent, 0, -1):
            ind[i] += ind[i - 1]
            ind[i - 1] = 0
    last = st
    # print(ind)

ans = 0
for i in range(indent + 1):
    ans += ind[i]
    ans %= MOD
print(ans)

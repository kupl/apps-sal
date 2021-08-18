import sys
read = sys.stdin.read
readline = sys.stdin.readline

N = int(readline())
aa = readline().strip()
ab = readline().strip()
ba = readline().strip()
bb = readline().strip()
nxt = [aa, ab, ba, bb]

n = 10
ans = [0] * n
ans[2] = 1
d = {"AB"}
k = ["AA", "AB", "BA", "BB"]
for i in range(3, n):
    nd = set()
    for v in d:
        for j in range(i - 2):
            idx = k.index(v[j:j + 2])
            c = v[:j + 1] + nxt[idx] + v[j + 1:]
            nd.add(c)
    d = nd
    ans[i] = len(d)


MOD = 10**9 + 7
r = (ans[2], ans[3], ans[4], ans[5])
if r == (1, 1, 1, 1):
    print((1))
elif r == (1, 1, 2, 4):
    if N == 2:
        print((1))
    else:
        print((pow(2, N - 3, MOD)))
elif r == (1, 1, 2, 3):
    x, y = 0, 1
    for i in range(N - 2):
        x, y = y, (x + y) % MOD
    print((y % MOD))

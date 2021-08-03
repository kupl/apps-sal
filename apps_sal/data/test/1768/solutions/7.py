import sys
input = sys.stdin.readline
N = int(input())
S = list(map(lambda x: ord(x) - ord("a"), list(input())[: -1]))
res = [[0] * (N + 1) for _ in range(26)]
for c in range(26):
    for l in range(N):
        x = 0
        for r in range(l + 1, N + 1):
            x += S[r - 1] != c
            res[c][x] = max(res[c][x], r - l)
    for i in range(N):
        res[c][i + 1] = max(res[c][i + 1], res[c][i])
for _ in range(int(input())):
    x, s = input().split()
    x = int(x)
    s = ord(s) - ord("a")
    print(res[s][x])

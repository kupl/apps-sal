import sys
import math

#https://atcoder.jp/contests/agc008/submissions/15248942
sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inm = lambda: map(int, sys.stdin.readline().split())
inl = lambda: list(inm())
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))

ans = "Yes"
N = ini()
words = []
for _ in range(N):
    words.append(input())


if len(words) != len(set(words)):
    ans = "No"

for i in range(N-1):
    if words[i][len(words[i])-1] != words[i+1][0]:
        ans = "No"

print(ans)



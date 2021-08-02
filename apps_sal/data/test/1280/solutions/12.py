import collections as cc
import sys
input = sys.stdin.readline
I = lambda: list(map(int, input().split()))
S = lambda: list(input().strip())
s = S()
t = S()
k, = I()
ans = 0
prev = ''
ss = sorted([s[i:] for i in range(len(s))])
for j in ss:
    now = 0
    f = 0
    for i in range(len(j)):
        if i >= len(prev) or j[i] != prev[i]:
            f = 1
        now += t[ord(j[i]) - ord('a')] == '0'
        if now > k:
            break
        if f:
            ans += 1
    prev = j
print(ans)

import sys
sys.setrecursionlimit(10 ** 6)
s = list(str(input()))
t = list(str(input()))
s.sort()
t.sort(reverse=True)
s = ''.join(s)
t = ''.join(t)
ans = sorted([s, t])
if ans[0] == t:
    print('No')
else:
    print('Yes')

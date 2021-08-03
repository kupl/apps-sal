from sys import stdin
S = stdin.readline().rstrip()
if S == 'RSR':
    ans = 1
else:
    ans = S.count('R')
print(ans)

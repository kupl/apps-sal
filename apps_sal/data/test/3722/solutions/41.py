import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

MOD = 10**9 + 7

N = int(input())
Caa = int(input().rstrip() != 'A')
Cab = int(input().rstrip() != 'A')
Cba = int(input().rstrip() != 'A')
Cbb = int(input().rstrip() != 'A')
C = Caa * 8 + Cab * 4 + Cba * 2 + Cbb

ptns = [1, 1, 1, 1, 4, 1, 3, 1, 3, 3, 4, 4, 4, 1, 3, 1]

ans3s = [1, 1, 1]
for i in range(N + 10):
    ans = ans3s[-2] + ans3s[-1]
    ans3s.append(ans % MOD)
# print('# ans3s:', ans3s, file=sys.stderr)
ans4s = [1, 1, 1]
for i in range(N + 10):
    ans = ans4s[-1] * 2
    ans4s.append(ans % MOD)
# print('# ans4s:', ans4s, file=sys.stderr)

ptn = ptns[C]
# print('# C:', C, '/ ptn:', ptn, file=sys.stderr)
if ptn == 1:
    ans = 1
elif ptn == 3:
    ans = ans3s[N - 1]
else:
    ans = ans4s[N - 1]

print((ans % MOD))

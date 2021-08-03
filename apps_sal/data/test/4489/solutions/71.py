N = int(input())
S = []
for i in range(N):
    s = input()
    S.append(s)

M = int(input())
T = []
for i in range(M):
    t = input()
    T.append(t)

ans = -1
x = 0
for i in S:
    x = S.count(i) - T.count(i)
    ans = max(ans, x)

if ans < 0:
    ans = 0

print(ans)

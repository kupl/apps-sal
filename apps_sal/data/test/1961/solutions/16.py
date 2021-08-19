"""n,L,a=map(int,input().split())
#s=[int(x) for x in input().split()]
ed=0
ct=0
for j in range(0,n):
    t,l=map(int,input().split())
    ct=ct+((t-ed)//a)
    ed=t+l
t=L
ct=ct+((t-ed)//a)
print(ct)"""
(n, m) = list(map(int, input().split()))
dp = [[-1 for i in range(m)] for j in range(n)]
dp2 = [[-1 for i in range(m)] for j in range(n)]
for i in range(0, n):
    s = input()
    for j in range(0, m):
        if s[j] == '.':
            dp[i][j] = -1
        else:
            dp[i][j] = s[j]
for i in range(0, n - 2):
    for j in range(0, m - 2):
        p = 0
        c = 0
        for k in range(i, i + 3):
            for h in range(j, j + 3):
                p = p + 1
                if p != 5:
                    if dp[k][h] == '#':
                        c = c + 1
        if c == 8:
            p = 0
            for k in range(i, i + 3):
                for h in range(j, j + 3):
                    p = p + 1
                    if p != 5:
                        dp2[k][h] = '#'
if dp == dp2:
    print('YES')
else:
    print('NO')

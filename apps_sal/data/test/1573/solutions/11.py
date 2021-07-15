#In the name of Allah

from sys import stdin, stdout
input = stdin.readline

n, h = list(map(int, input().split()))
f = sorted([list(map(int, input().split())) for i in range(n)])

ans = 0
fc = f[0][1]
start = 0

for i in range(1, n):
        while f[i][0] - f[start][0] >= h:
                
                ans = max(ans, fc)
                fc -= f[start][1]
                start += 1
                #print(f[start],fc, i)

        fc += f[i][1]
        ans = max(ans, fc)
        #print(fc, ans)
stdout.write(str(max(ans, fc)))


n = int(input())
s = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
f1 = [0 for x in range(0,3005)]
f = [[99999999999 for x in range(0,3005)] for i in range(1,4)]
f.insert(0,f1)
for i in range(0,n):
    f[1][i] = c[i]
for x in range(2,4):
    for i in range(x-1,n):
        for j in range(0,i):
            if s[j] < s[i] and f[x-1][j] != 99999999999:
                f[x][i] = min(f[x-1][j]+c[i], f[x][i])
for i in range(1,n):
    f[3][i] = min(f[3][i-1],f[3][i])
if f[x][i] != 99999999999:
    print(f[x][i])
else:
    print(-1)

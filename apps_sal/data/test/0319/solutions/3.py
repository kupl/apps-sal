'''n = int(input())
a = list(map(int,input().split()))
t = 0
t2 = 0
for i in range(n//2):
    t+=abs(2*i+1-a[i])
    t2+=abs(2*i+2-a[i])
print(min(t,t2))
'''
n, m = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(input())
f = [True] * n
for j in range(m):
    l = -1
    c = 0
    for i in range(n):
        if a[i][j] == '1':
            l = i
            c += 1
    if c == 1:
        f[l] = False
if True in f: print('YES')
else: print('NO')

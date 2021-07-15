k = int(input())
a = []
for i in range(k):
    n = int(input())
    b = [int(i) for i in input().split()]
    s = sum(b)
    for j in range(n):
        x = s-b[j]
        a.append([x,i,j])
f = True
a = sorted(a)
for i in range(1,len(a)):
    if a[i][0] == a[i-1][0] and a[i][1]!=a[i-1][1]:
        f = False
        print('YES')
        print(a[i][1]+1,a[i][2]+1)
        print(a[i-1][1]+1, a[i-1][2]+1)
        break
if f:
    print('NO')

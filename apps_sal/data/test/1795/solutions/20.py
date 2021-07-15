n=int(input())
l = list(map(int,input().split()))
for i in range(n):
    if l[l[l[i-1]-1]-1]==i:
        print('YES')
        quit()
print('NO')


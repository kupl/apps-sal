n,m=list(map(int,input().split()))
mn=0
for i in range(n):
    mas=list(map(int,input().split()))
    if mn<min(mas):
        mn=min(mas)
print(mn)



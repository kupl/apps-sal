n=int(input())
mas=list(map(int,input().split(" ")))
mas.sort()
res=0
for i,x in enumerate(mas):
    res+=(abs(i-x+1))
print(res)

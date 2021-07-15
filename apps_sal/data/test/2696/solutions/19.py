# Good judgment comes from experience, and experience comes from bad judgment. Rita Mae Brown
# by : Blue Edge - Create some chaos

n=int(input())
a=list(map(int,input().split()))
i=n-1
while i+1:
    if a[i]!=a[-1]:
        break
    i-=1
print(i+2)


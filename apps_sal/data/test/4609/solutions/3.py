N = int(input())
A = [int(input()) for _ in range(N)]

d = {}
#key設定
for i in A:
    d[i]=0
#数字keyが偶数回出たら0,奇数回出たら1になるようにvalueを設定
for i in A:
    if d[i]==1:
        d[i]=0
    else:
        d[i]=1
    
print(sum(d.values()))

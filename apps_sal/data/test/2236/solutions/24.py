n=int(input())
l=list(map(int, input().split()))
sum=0
d=dict()
for i in range(n):
    sum += l[i]
    if sum not in d.keys():
        d[sum] = 1
    else:
        d[sum]+=1
print(n-max(d.values()))

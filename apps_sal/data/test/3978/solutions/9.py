n=int(input())
a=[int(i) for i in input().split()]
a.sort()
tot = 0
d={}
for i in range(len(a)):
    if a[i] not in d:
        tot+=1
        for j in range(i+1,len(a),1):
            if a[j]%a[i] == 0:
                d[a[j]]=1
print(tot)

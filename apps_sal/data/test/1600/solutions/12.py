from collections import Counter as Cnt
n = int(input())
data = tuple(map(int,input().split()))
datasorted = sorted(data)

i = 0
a = Cnt()
b = Cnt()
ans = 0
for i in range(n):
    a[data[i]]+=1
    b[datasorted[i]]+=1
    if a==b:
        ans+=1
        a,b=Cnt(),Cnt()
print(ans)

n = int(input())
a=list(map(int, input().split()))
s=set(a)
if len(s)==1 and 1 in s:
    print(n)
    return
k = 0
ma = 0
for i in range(n):
    if a[i]:
        k+=1
    else:
        ma=max(ma, k)
        k = 0
for i in range(n):
    if a[i]:
        k+=1
    else:
        ma=max(ma, k)
        k = 0
print(max(ma, k))

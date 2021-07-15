# cook your dish here
n = int(input())
a = list(map(int,input().split()))
a.sort()
count=0
if a[0]!=0:
    count+=1
for i in range(1,n):
    if a[i-1]!=a[i]:
        count+=1
print(count)

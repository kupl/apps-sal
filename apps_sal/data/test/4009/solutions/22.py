n,x,y=map(int,input().split())
a=input()
count=0
a=a[::-1]
for i in range(y):
    if a[i]=='1':
        count+=1
if a[y]=='0':
    count+=1
for i in range(y+1,x):
    if a[i]=='1':
        count+=1
print(count)

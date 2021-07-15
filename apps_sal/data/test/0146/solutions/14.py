from sys import stdin,stdout

I = stdin.readline
P = stdout.write

n,k = map(int,I().split())
arr = [int(x) for x in I().split()]

e = 0
s = 0
ans = 0
for i in arr:
    if(i == -1):
        s+=1
    else:e+=1

for i in range(0,k):
    ce = 0
    cs = 0
    for j in range(i,n,k):
        if(arr[j] == -1):
            cs+=1
        else:
            ce+=1
    x = e-ce
    y = s - cs
    if(abs(x-y)>ans):ans = abs(x-y)
print(ans)

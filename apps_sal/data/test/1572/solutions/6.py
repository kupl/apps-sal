n = int(input())
a = list(map(int,input().split()))
c = [False]*n
for i in range(2,n):
    if a[i]==a[i-1]+a[i-2]:
        c[i] = True
m = 0
j = 0
i = 2
l = 0
while i < n:
    if c[i] == False:
        if l > m:
            m = l
            j = i-l+1
        l = 0
    else:
        l+=1
    i+=1
if l != 0 and l>m:
    m = l
    j = i-l
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    print(m+2)

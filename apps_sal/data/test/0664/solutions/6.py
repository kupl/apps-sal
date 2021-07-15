n = int(input())
a = input().split(' ')
pre = int(a[0])
pos = n
for i in range(1,n):
    x = int(a[i])
    if x<pre:
        pre = x
        pos = i
        break
    pre = x
if pos==n:
    print(0)
else:
    ans = 0
    for j in range(pos,n):
        x = int(a[j])
        if x<pre:
            ans = -1
            break
        pre = x
    if ans==-1:
        print(-1)
    elif int(a[n-1])>int(a[0]):
        print(-1)
    else:
        print (n-pos)

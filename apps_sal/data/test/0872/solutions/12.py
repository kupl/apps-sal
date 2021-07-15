n=int(input())
a=list(map(int,input().split()))
odd=0
even=0
for i in a:
    if i&1:
        odd += 1
    else:
        even += 1
if odd == n or even == n:
    for i in range(len(a)):
        print(a[i],end=" ")
else:
    a=sorted(a)
    for i in range(len(a)):
        print(a[i],end=" ")
    

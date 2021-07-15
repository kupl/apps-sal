n,k = map(int,input().split())
a = list(map(int,input().split()))
t,ans =2**40,0
while t:
    c = sum([(a[i]&t)//t for i in range(n)]) #a[i]のある桁における1の数
    if c>=n-c or k<t: ans += t*c
    else: ans += t*(n-c);k-=t
    t = t>>1
print(ans)

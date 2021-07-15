n=int(input())
a={'M':0,'S':0,'L':0,'XL':0,'XXL':0,'XXXL':0,'XS':0,'XXS':0,'XXXS':0}
b={'M':0,'S':0,'L':0,'XL':0,'XXL':0,'XXXL':0,'XS':0,'XXS':0,'XXXS':0}
ans=0
for i in range(n):
    a[input()]+=1
for i in range(n):
    b[input()]+=1
for i in a:
    a[i]=max(a[i]-b[i],0)
for i in a:
    ans+=a[i]
print(ans)
    


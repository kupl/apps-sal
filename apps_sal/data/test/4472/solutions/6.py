n=int(input())
a=input()
b=input()
count=0
for i in range(n//2):
    d={}
    for c in [a[i],a[n-i-1],b[i],b[n-i-1]]:
        d[c]=d.get(c,0)+1
    if a[i]==a[n-i-1]==b[i]==b[n-i-1]:
        continue
    count+=2
    if a[i]==a[n-i-1] and b[i]!=b[n-i-1] and a[i]!=b[i] and a[i]!=b[n-i-1]:
        continue
    for v in d.values():
        if v>=2:count-=1
if n%2==1 and a[n//2]!=b[n//2]:
    count+=1
print(count)

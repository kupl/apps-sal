n=int(input())
ar=sorted(list(map(int,input().split())))
mx=-float('inf')
for x in ar:
    if x<0:
        mx=x
        continue
    el=round(x**0.5)
    if el**2!=x:
        mx=x
print(mx)

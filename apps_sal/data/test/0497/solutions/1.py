

def ria():
    return [int(i) for i in input().split()]


mx=0
n=ria()[0]
ar=ria()
for i in range(n):
    if ar[i]!=ar[0]:
        mx=max(i,mx)
    if ar[i]!=ar[n-1]:
        mx=max(n-1-i,mx)
print(mx)

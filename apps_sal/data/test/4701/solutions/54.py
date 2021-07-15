#76B
n=int(input())
k=int(input())
f=1
for i in range(0,n):
    if f*2<f+k:
        f=f*2
    else:
        f=f+k
print(f)

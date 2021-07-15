# input segment
w,l = list(map(int,input().split()))
a=list(map(int,input().split()))

# computer minimal segemnt of length l, and a temp variable
minsegment=s=sum(a[:l])

# calculate every l segment min value,
for i in range(1,w-l):
    s=s-a[i-1]+a[i+l-1]
    minsegment = min(s,minsegment)

print(minsegment)


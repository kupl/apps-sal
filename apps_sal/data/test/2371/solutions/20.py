n,z,w = map(int,input().split())
l = list(map(int,input().split()))
if n==1:
    print(abs(l[-1]-w))
else:
    print(max(abs(l[-1]-w),abs(l[-1]-l[-2])))

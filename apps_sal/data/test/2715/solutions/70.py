k = int(input())
q = k//50
r = k%50
print(50)
a = [0]*50
for i in range(50):
    if i < r:
        a[i] = 100+q-r
        # a[i] = 49+50*(q+1)-49*q-(r-1)
    else:
        a[i] = 49+q-r
        # a[i] = 49+50*q-49*q-r
print(*a)

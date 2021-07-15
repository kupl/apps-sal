n,k = map(int, input().split())
a = list(map(int, input().split()))

if k > n:
    print(max(a))
    return

st = 0
while st < k:
    if a[0] > a[1]:
        st+=1
        a.append(a[1])
        del a[1]
    else:
        st = 1
        a.append(a[0])
        del a[0]
        
print(a[0])

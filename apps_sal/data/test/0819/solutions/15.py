n , k = [int(z) for z in input().split()]
a = [int(z) for z in input().split()]
kek = max(a)
if k > 2:
    print(kek)
    return
if k > 1:
    print(max(a[0], a[-1]))   
else:
    print(min(a))

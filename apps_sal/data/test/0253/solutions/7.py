def ans(k1, k2, k3):
    if k1 == 1:
        return 'YES'
    if k1 == 2 and k2 == 2:
        return 'YES'
    if k1 == 3 and k2 == 3 and (k3 == 3):
        return 'YES'
    if k1 == 2 and k2 == 4 and (k3 == 4):
        return 'YES'
    return 'NO'


(a, b, c) = [int(i) for i in input().split()]
k1 = min(a, b, c)
k3 = max(a, b, c)
k2 = a + b + c - k1 - k3
print(ans(k1, k2, k3))

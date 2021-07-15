k2, k3, k5, k6 = map(int, input().split())

a = min(k2, k5, k6)
b = min(k3, k2-a)
print(256*a+32*b)

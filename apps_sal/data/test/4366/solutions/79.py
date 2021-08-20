a = list(map(int, input().split()))
b = a[0] + a[1]
if b >= 24:
    b -= 24
print(b)

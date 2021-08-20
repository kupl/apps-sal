n = int(input())
a = list(map(int, input().split()))
prod = a[0]
for A in a[1:]:
    prod *= A
sumprod = 0
for A in a:
    sumprod += prod // A
print(prod / sumprod)

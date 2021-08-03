n, k = map(int, input().split())
ds = [d for d in input().split()]
while any(c in ds for c in str(n)):
    n += 1
print(n)

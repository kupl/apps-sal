(n, r) = list(map(int, input().split()))
if n < 10:
    r += (10 - n) * 100
print(r)

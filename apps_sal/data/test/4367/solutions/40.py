(n, p) = map(int, input().split())
if n < 10:
    rate = p + 100 * (10 - n)
else:
    rate = p
print(rate)

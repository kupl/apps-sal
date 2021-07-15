n, k = list(map(int, input().split()))
h = k - 1
while True:
    if n % h == 0:
        break
    h -= 1
print(n // h * k + h)

(n, x, t) = list(map(int, input().split()))
s = n // x + 1
if n % x == 0:
    s -= 1
print(s * t)

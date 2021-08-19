(n, x, t) = list(map(int, input().split()))
if n % x == 0:
    answer = n // x * t
else:
    answer = (n // x + 1) * t
print(int(answer))

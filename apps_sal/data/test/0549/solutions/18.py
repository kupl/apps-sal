n = int(input())
(min_sum, a, b) = (n, 0, 0)
for i in range(1, int(n ** (1 / 2) + 1)):
    if not n % i and min_sum > abs(i - n // i):
        (a, b) = (i, n // i)
        min_sum = abs(a - b)
print(a, b)

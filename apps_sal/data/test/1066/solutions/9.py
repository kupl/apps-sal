(n, k) = [int(x) for x in input().split()]
even = n // 2
odd = n - even
if k <= odd:
    print(2 * k - 1)
else:
    print(2 * (k - odd))

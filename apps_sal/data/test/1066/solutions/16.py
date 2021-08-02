n, k = list(map(int, input().split()))
half = int(n / 2) + n % 2
if k > half:
    k -= half
    print(2 * k)
else:
    print(2 * k - 1)

n, k = list(map(int, input().split()))
if n == 1 or k == 0 or k == n:
    print(0, 0)
elif n // k < 3:
    print(1, n - k)
else:
    print(1, 2 * k)

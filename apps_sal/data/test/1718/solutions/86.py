(n, k) = map(int, input().split())
a = list(map(int, input().split()))
print((n - 1) // (k - 1) if (n - 1) % (k - 1) == 0 else (n - 1) // (k - 1) + 1)

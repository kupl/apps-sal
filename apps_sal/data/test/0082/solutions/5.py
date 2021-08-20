(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
print(max(0, 2 * n * k - n - 2 * sum(a)))

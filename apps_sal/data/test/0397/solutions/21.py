(n, k) = [int(i) for i in input().split()]
a = pow(1 + 2 * k + 2 * n, 0.5) - 1
print(n - int(a))

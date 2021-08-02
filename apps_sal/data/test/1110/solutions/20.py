n = int(input())
print(n + sum(i * (n - i) for i in range(1, n)))

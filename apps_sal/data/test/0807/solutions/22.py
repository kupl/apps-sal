(n, c) = list(map(int, input().split()))
x = list(map(int, input().split()))
print(max(0, max((x[i] - x[i + 1] - c for i in range(0, n - 1)))))

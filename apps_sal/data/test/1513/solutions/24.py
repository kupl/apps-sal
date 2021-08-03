n, m, k = list(map(int, input().split()))
b = list(map(int, input().split()))

print((b[n - 1] - b[0] + 1 - sum(sorted([b[i] - b[i - 1] - 1 for i in range(1, n)], reverse=True)[0:k - 1])))

N = int(input())
X = list(map(int, input().split()))
a = sum(X)
b = 0
for num in X:
    b += num ** 2
ans = float('inf')
for i in range(1, 101):
    ans = min(ans, N * i * i - 2 * a * i + b)
print(ans)

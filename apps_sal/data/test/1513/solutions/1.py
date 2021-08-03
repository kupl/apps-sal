n, m, k = map(int, input().split())
b = list(map(int, input().split()))
c = []
for i in range(n - 1):
    c.append(b[i + 1] - b[i] - 1)
c = list(sorted(c))[::-1]
print(b[n - 1] - b[0] + 1 - sum(c[:k - 1]))

(n, k) = map(int, input().split())
m = []
for i in range(n):
    m.append(int(input()))
rest = k - sum(m)
print(n + rest // min(m))

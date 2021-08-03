a = int(input())
b = [0] * (a + 1)
for _ in " " * (a - 1):
    u, v = map(int, input().split())
    b[u] += 1
    b[v] += 1
print(sum((i * (i - 1)) // 2 for i in b))

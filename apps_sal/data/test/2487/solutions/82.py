n = int(input()) + 1
a = (n**3 - n) // 6
for _ in range(n - 2):
    u, v = map(int, input().split())
    a -= min(u, v) * (n - max(u, v))
print(a)

n, x, y = list(map(int, input().split()))
S = set()
for i in range(n):
    a, b = list(map(int, input().split()))
    S.add((a - x) / (b - y) if b - y != 0 else float("INF"))
print(len(S))

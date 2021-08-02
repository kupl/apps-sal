n, m = list(map(int, input().split()))
pen = list(map(int, input().split()))
wyn = [0] * n
pen.sort()
dupa = [0] * n
for i in range(m):
    dupa[i] = pen[i]
for i in range(m, n):
    dupa[i] = dupa[i - m] + pen[i]

wyn[0] = dupa[0]
for i in range(1, n):
    wyn[i] = wyn[i - 1] + dupa[i]
print(*wyn)

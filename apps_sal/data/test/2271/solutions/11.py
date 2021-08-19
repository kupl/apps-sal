I = input
d = [0] * 10010
for _ in '0' * (int(I()) - 1):
    (x, y) = map(int, I().split())
    d[x] += 1
    d[y] += 1
print(sum((i * (i - 1) for i in d)) // 2)

a, b, k = map(int, input().split())
n = []
for i in range(k):
    if a + i > b:
        break
    n.append(a + i)
for j in range(k):
    if b - k + 1 + j < a:
        break
    if n.count(b - k + 1 + j) <= 0:
        n.append(b - k + 1 + j)
[print(num) for num in n]

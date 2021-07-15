n, m = map(int, input().split())
seg = [0] * (m + 1)
seg[0] = 1
for i in range(n):
    a, b = map(int, input().split())
    for j in range(a, b + 1):
        seg[j] = 1

rec = []
for i in range(m + 1):
    if seg[i] != 1:
        rec.append(i)

print(len(rec))
print(" ".join(map(str, rec)))

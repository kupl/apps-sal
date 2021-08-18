n = int(input())
p = []
for _ in range(0, n):
    p.append(int(input()))
print(int(sum(p) - max(p) / 2))

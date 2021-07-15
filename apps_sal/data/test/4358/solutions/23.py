N = int(input())
p = []
for _ in range(0, N):
    p.append(int(input()))

print(int(sum(p) - max(p) / 2))

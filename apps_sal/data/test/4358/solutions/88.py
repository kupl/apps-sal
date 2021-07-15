N = int(input())
p = []
for i in range(N):
    p.append(int(input()))

Expensive = max(p)
p.remove(Expensive)
print(Expensive // 2 + sum(p))

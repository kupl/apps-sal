N = int(input())
p = []
for i in range(N):
    p.append(int(input()))
p.sort()
cost = 0
for i in range(N - 1):
    cost += p[i]
print(cost + p[N - 1] // 2)

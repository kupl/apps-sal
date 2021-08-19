N = int(input())
p = []
for i in range(N):
    p.append(int(input()))
print(sum(p) - max(p) // 2)

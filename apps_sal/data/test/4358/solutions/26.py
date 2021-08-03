N = int(input())
p = []
for i in range(N):
    p.append(int(input()))
p.sort()
ans = sum(p) - p[-1] // 2
print(ans)

N = int(input())
p = []
for i in range(N):
    p.append(int(input()))
max_p = max(p)
ans = int(max_p / 2) + sum(p) - max_p
print(ans)

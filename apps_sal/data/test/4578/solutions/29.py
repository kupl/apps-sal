(n, x) = map(int, input().split())
m = []
for i in range(n):
    m.append(int(input()))
cnt = (x - sum(m)) // min(m)
ans = n + cnt
print(ans)

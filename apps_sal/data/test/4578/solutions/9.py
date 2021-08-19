(n, x) = list(map(int, input().split()))
l = []
ans = 0
for i in range(n):
    l.append(int(input()))
x -= sum(l)
ans += n
ans += x // min(l)
print(ans)

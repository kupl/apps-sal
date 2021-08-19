(x, n) = list(map(int, input().split()))
p = list(map(int, input().split()))
gap = x
ans = 0
for y in range(0, 102):
    if y not in p:
        if abs(x - y) < gap:
            gap = abs(x - y)
            ans = y
print(ans)

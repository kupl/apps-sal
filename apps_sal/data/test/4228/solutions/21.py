n, l = map(int, input().split())
s = sum(range(l, l + n))
ans = 1000
for i in range(l, l + n):
    if abs(i) <= abs(ans):
        ans = i
print(s - ans)

n = int(input())
ans = -10 ** 18
for a in map(int, input().split()):
    if a < 0:
        ans = max(ans, a)
        continue
    t = int(a ** 0.5)
    if not ((t - 1) ** 2 == a or t ** 2 == a or (t + 1) ** 2 == a):
        ans = max(ans, a)
print(ans)

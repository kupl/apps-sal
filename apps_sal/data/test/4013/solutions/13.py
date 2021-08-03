n = int(input())
a = sorted(list(map(int, input().split())))
ans = 0
if n > 2:
    ans = min(a[-2] - a[0], a[-1] - a[1])
print(ans)

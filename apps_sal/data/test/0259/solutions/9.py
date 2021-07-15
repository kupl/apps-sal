n, t = list(map(int, input().split()))
ans = 10**6
ansi = 0
for i in range(n):
    s, d = list(map(int, input().split()))
    s = max(0, t - s + d - 1) // d * d + s
    # print(s)
    if ans > s:
        ans = s
        ansi = i
print(ansi+1)


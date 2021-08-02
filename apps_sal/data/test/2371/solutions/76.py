N, Z, W = map(int, input().split(" "))        # Z は要らん子

a = list(map(int, input().split(" ")))

if N == 1:
    ans = abs(a[-1] - W)
else:
    ans = max(abs(a[-1] - a[-2]), abs(a[-1] - W))


print(ans)

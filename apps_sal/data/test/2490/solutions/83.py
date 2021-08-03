N = input()
N = N[::-1] + "0"
ans = 0
up = 0
for i, n in enumerate(N):
    d = int(n) + up
    if 5 < d or (d == 5 and i < len(N) - 1 and int(N[i + 1]) >= 5):
        ans += (10 - d)
        up = 1
    else:
        ans += d
        up = 0
print(ans)

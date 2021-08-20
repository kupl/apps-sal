n = (360 + int(input()) % 360) % 360
ans = 0
bres = n
for i in range(1, 5):
    d = (360 + (n - i * 90) % 360) % 360
    if min(d, 360 - d) < min(bres, 360 - bres):
        bres = d
        ans = i
print(ans)

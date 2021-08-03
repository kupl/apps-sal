[a, ta] = [int(i) for i in input().split()]
[b, tb] = [int(i) for i in input().split()]
[h, m] = [int(i) for i in input().split(':')]
xa = h * 60 + m
ya = xa + ta
ans = 0
for xb in range(300, 24 * 60, b):
    yb = xb + tb
    if(max(xa, xb) < min(ya, yb)):
        ans += 1
print(ans)

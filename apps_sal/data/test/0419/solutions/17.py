n = int(input(), 2)
t = 1
ans = 0

for i in range(101):
    if t < n:
        ans += 1
    t *= 4

print(ans)

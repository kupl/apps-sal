n = int(input(), 2)
ans = 0
t = 1
while t < n:
    ans += 1
    t *= 4
print(ans)

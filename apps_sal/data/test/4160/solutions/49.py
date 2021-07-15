x = int(input())
ans = 0
x2 = 100
for _ in range(1, 3761):
    if x2 < x:
        x2 += x2 // 100
        ans += 1

print(ans)

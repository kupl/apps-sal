b = int(input())
g = int(input())
n = int(input())
ans = 0
for i in range(n + 1):
    bb = i
    gg = n - i
    if bb <= b and gg <= g:
        ans += 1
print(ans)

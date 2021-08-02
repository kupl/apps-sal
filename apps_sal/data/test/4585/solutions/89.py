X = int(input())
m = 0
ans = 0
for i in range(1, X + 1):
    if X <= m:
        break
    m += i
    ans += 1
print(ans)

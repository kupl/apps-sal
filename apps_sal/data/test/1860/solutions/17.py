n = int(input())
ans = 0
mult = 1
for i in range(1, n+1):
    mult *= 2
    ans += mult
print(ans)


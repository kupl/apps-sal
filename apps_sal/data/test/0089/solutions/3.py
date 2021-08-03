n = int(input())
ans = 0
if(n % 2 == 0):
    ans += (n // 2) * (n // 2 + 1)
else:
    ans += ((n + 1) // 2)**2

print(ans)

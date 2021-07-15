n = int(input())

ans = 0

for i in range(n // 2 + (0 if n % 2 == 0 else 1)):
    l = n - 2 * i
    if l <= 0:
        break
    ans += l

print(ans)
    


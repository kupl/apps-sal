n = int(input())
if n % 1000 == 0:
    ans = 0
else:
    ans = (n // 1000 + 1) * 1000 - n
print(ans)

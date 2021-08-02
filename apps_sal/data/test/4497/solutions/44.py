n = int(input())
ans = 2
while n > ans:
    ans *= 2
if n < ans:
    ans //= 2
print(ans)

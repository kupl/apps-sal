n = int(input())
ans = 1
for i in range(n):
    ans *= i + 1
for i in range(n // 2):
    ans //= i + 1
    ans //= i + 1
gg = 1
for i in range(n//2 - 1):
    gg *= i + 1
ans *= gg * gg
ans//= 2
print(ans)


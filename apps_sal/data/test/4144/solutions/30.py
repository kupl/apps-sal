n = int(input())
ans = 0

if n == 1:
    ans = 0
else:
    ans = ((10**n)%(10**9+7) - ((2*9**n)%(10**9+7) - (8**n)%(10**9+7)))%(10**9+7)

print(ans)

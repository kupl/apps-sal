n = int(input())
ans = []
mult = 1
while n > 3:
    ans += [mult] * (n - n // 2)
    n //= 2
    mult *= 2
if n == 3:
    ans += [mult, mult, mult * 3]
elif n == 2:
    ans += [mult, mult * 2]
else:
    ans += [mult]
print(*ans)

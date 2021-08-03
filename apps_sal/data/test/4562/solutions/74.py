n = int(input())
p = int(n**0.5)
a = 1
ans = 1
while a <= p:
    if a**2 <= n:
        ans = max(ans, a**2)
    a += 1
print(ans)

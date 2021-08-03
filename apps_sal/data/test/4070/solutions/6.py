n = int(input())

a = []
if n == 0:
    a.append(0)
while n > 0:
    a.append(n % 16)
    n //= 16

b = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1, 1, 2, 0, 1, 0, 0]

ans = 0
for x in a:
    ans += b[x]
print(ans)

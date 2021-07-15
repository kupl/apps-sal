n = int(input())
divs = set()
div = 2
while div <= n ** 0.5:
    if n % div == 0:
        divs.add(div)
        n //= div
    else:
        div += 1
if n > 1:
    divs.add(n)
ans = 1
for div in divs:
    ans *= div
print(ans)

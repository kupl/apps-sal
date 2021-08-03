import math
n = int(input())

# Prime factoring
pf = []
for i in range(2, math.ceil(n**0.5) + 1):
    temp = 0
    while n % i == 0:
        n /= i
        temp += 1
    if temp:
        pf.append(temp)
    if n == 1:
        break
if n != 1:
    pf.append(1)

ans = 0
for i in range(len(pf)):
    j = 1
    while pf[i] - j >= 0:
        ans += 1
        pf[i] -= j
        j += 1
print(ans)

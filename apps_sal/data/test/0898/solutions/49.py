import math
(n, m) = map(int, input().split())
fact = []
ans = 1
MAX = int(math.sqrt(m)) + 1
for i in range(1, MAX):
    if m % i == 0:
        fact.append(i)
        if i != m // i:
            fact.append(m // i)
fact.sort()
for x in fact:
    if m < n * x:
        break
    ans = x
print(ans)

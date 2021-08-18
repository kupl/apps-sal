import math
n = int(input())
a = list(map(int, input().split()))
d = {0: 1}
m = 1
ans = 0
for i in a:
    divisors = []
    for j in range(1, min(m, int(math.sqrt(i))) + 1):
        if i % j == 0:
            k = int(i / j)
            divisors.append(j)
            if j != k and k <= m:
                divisors.append(k)
    new_d = {0: 1}
    for j in divisors:
        ans = (ans + d[j - 1]) % 1000000007
        new_d[j] = d.get(j, 0) + d[j - 1]
        if j == m:
            m = m + 1
    for j in new_d:
        d[j] = new_d[j]
print(ans)

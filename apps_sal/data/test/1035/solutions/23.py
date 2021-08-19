import math
(a, b) = map(int, input().split())
ans = [1]
c = math.gcd(a, b)
for i in range(2, int(c ** (1 / 2)) + 1):
    if c % i == 0:
        while c % i == 0:
            c //= i
        ans.append(i)
if c != 1:
    ans.append(c)
print(len(ans))

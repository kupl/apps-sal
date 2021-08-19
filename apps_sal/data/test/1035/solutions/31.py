import math
(a, b) = map(int, input().split())
x = math.gcd(a, b)
bun = [0] * int(math.sqrt(x) + 1)
bun[1] = 1
for i in range(2, len(bun)):
    while x % i == 0:
        if bun[i] == 0:
            bun[i] += 1
        x = x // i
ans = sum(bun)
if x > 1:
    ans += 1
print(ans)

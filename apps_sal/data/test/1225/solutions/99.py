import math
h = int(input())
(a, ans) = (0, 0)
while h > 1:
    h = math.floor(h / 2)
    a += 1
for i in range(a + 1):
    ans += 2 ** i
print(ans)

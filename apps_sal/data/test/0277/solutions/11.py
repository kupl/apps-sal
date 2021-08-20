import math
(n, a, b) = map(int, input().split())
i = 2
(a, b) = (min(a, b), max(a, b))
while True:
    if a <= n // i < b:
        break
    if a > n // i:
        a -= n // i
        b -= n // i
    i *= 2
ans = math.log(n, 2) - math.log(i, 2) + 1
if math.log(i, 2) == 1:
    print('Final!')
else:
    print(int(ans))

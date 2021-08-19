import math
(a, b) = map(str, input().split())
ab = int(a + b)
sq = math.sqrt(ab)
if sq % 1 < 0.01:
    sq2 = sq ** 2
    if sq2 == ab:
        ans = 'Yes'
    else:
        ans = 'No'
else:
    ans = 'No'
print(ans)

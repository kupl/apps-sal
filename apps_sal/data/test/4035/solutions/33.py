import math
(A, B) = map(int, input().split())
mini = max(math.ceil(A / 0.08), B * 10)
maxi = min(int((A + 1) / 0.08), (B + 1) * 10)
if mini >= maxi:
    print(-1)
else:
    print(mini)

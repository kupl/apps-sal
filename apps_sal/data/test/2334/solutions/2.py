import math
n = int(input())
rek = list(map(int, input().split()))
(mx, pay) = map(int, input().split())
ans = 0
for i in rek:
    if i > mx:
        ans += pay * math.ceil((i - mx) / (mx + pay))
print(ans)

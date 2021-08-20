import math
ntc = int(input())
for tcs in range(ntc):
    (s, i, e) = list(map(int, input().split()))
    if s + e > i:
        res = math.ceil((s + e - i) / 2)
        print(min(res, e + 1))
    else:
        print(0)

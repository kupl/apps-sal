import math
import io

nim, mike, kite = list(map(int, input().split()))
H = [int(input()) for _ in range(nim)]

OK = max(H)//kite+1
NG = 0

ans = OK
while OK-NG > 1:
    mid = (OK+NG)//2  # 試行する値
    cnt = 0

    for h in H:
        if h > mid*kite:
            cnt += math.ceil((h-mid*kite)/(mike-kite))

    if cnt <= mid:
        OK = mid
    else:
        NG = mid

print(OK)


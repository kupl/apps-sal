# Comment out -> using bisect ver. method
# import bisect
import math
N, H = list(map(int, input().split()))
swing = []
throw = []
for _ in range(N):
    sw, th = list(map(int, input().split()))
    swing.append(sw)
    throw.append(th)
swing.sort(reverse=True)
throw.sort(reverse=True)
'''
idx = bisect.bisect_right(throw, swing[0])
if idx == len(throw):
    print(math.ceil(H / swing[0]))
'''
if swing[0] >= throw[0]:
    print((math.ceil(H / swing[0])))
else:
    # throw = throw[idx:]
    cnt = 0
    damage_sum = 0
    while cnt < len(throw):
        if throw[cnt] <= swing[0]:
            break
        damage_sum += throw[cnt]
        cnt += 1
        if damage_sum >= H:
            print(cnt)
            return
    '''
    for i in reversed(throw):
        cnt += 1
        damage_sum += i
        if damage_sum >= H:
            print(cnt)
            return
    '''
    print((math.ceil(cnt + (H - damage_sum) / swing[0])))

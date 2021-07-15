def mn(ms):
    ret = min(ms)
    index = ms.index(ret)
    ms[index] = 101
    return [ret, index]
    
n, k = [int(i) for i in input().split()]
ms = [int(i) for i in input().split()]
mx = max(ms)
ret = []
days = 0
p = 0
for i in range(len(ms)):
    box = mn(ms)
    if days + box[0] <= k:
        days += box[0]
        ret.append(box[1] + 1)
        p += 1
print(p)
if ret != []:
    for i in ret:
        print(i, end = ' ')

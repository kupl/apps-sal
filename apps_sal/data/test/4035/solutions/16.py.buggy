a, b = [int(i) for i in input().split()]
idx = 0
rangein = False
while(True):
    aa = int(idx * 0.08)
    bb = int(idx * 0.1)
    if aa == a and bb == b:
        print(idx)
        return
    elif aa == a or bb == b:
        rangein = True
    elif rangein and aa != a and bb != b:
        print(-1)
        return
    idx += 1

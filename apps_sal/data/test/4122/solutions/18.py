import math
(H, n) = [int(i) for i in input().split(' ')]
d = [int(i) for i in input().split(' ')]
H_cur = H
dead = False
d_acc = [0]
for i in range(n):
    d_acc.append(d_acc[-1] + d[i])
    H_cur += d[i]
    if H_cur <= 0:
        print(i + 1)
        dead = True
        break
if not dead:
    if d_acc[-1] >= 0:
        print(-1)
    else:
        d_acc_min = min(d_acc)
        r = int(math.ceil((H + d_acc_min) / -d_acc[-1]))
        H_cur = H + r * d_acc[-1]
        for i in range(n):
            H_cur += d[i]
            if H_cur <= 0:
                print(r * n + i + 1)
                break

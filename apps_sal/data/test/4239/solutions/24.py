import math
power_6 = [6 ** i for i in range(int(math.log(100000, 6)) + 1)]
power_9 = [9 ** i for i in range(int(math.log(100000, 9)) + 1)]
p = list(set(power_6 + power_9))
p.sort()
p.append(100001)

N = int(input())

idx = 0
cnt = [0]
i = 1
while i < N + 1:
    if p[idx] <= i < p[idx + 1]:
        c = 0
        if idx == 0:
            cnt.append(i)
        else:
            c = [cnt[i - p[j]] + 1 for j in range(idx + 1)]
            cnt.append(min(c))
        i += 1
    else:
        idx += 1

print(cnt[N])

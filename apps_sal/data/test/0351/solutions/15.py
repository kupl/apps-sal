import math


def I():
    return list(map(int, input().split()))


(n, k) = I()
a = list(I())
ans = 0
for task in sorted(a):
    if math.ceil(task / 2) <= k:
        k = max(task, k)
        continue
    else:
        while not math.ceil(task / 2) <= k:
            ans += 1
            k *= 2
        k = task
print(ans)

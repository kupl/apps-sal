n, c = map(int, input().split())
xv = []
for _ in range(n):
    x, v = map(int, input().split())
    xv.append((x, v))
r1 = [0]
r2 = [0]
px = 0
for x, v in xv:
    r1.append(r1[-1] + v - (x - px))
    r2.append(r2[-1] + v - 2 * (x - px))
    px = x
l1 = [0]
l2 = [0]
px = 0
for x, v in reversed(xv):
    x = c - x
    l1.append(l1[-1] + v - (x - px))
    l2.append(l2[-1] + v - 2 * (x - px))
    px = x


def accu_max(li):
    mx = -1
    for i in range(n + 1):
        if li[i] > mx:
            mx = li[i]
        else:
            li[i] = mx


accu_max(r1)
accu_max(r2)
accu_max(l1)
accu_max(l2)
ans = 0
for i in range(n + 1):
    ans = max(ans, r1[i] + l2[n - i])
    ans = max(ans, l1[i] + r2[n - i])
print(ans)

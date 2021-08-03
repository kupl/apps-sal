N = int(input())

t = [int(x) for x in input().split()]
vSection = [int(x) for x in input().split()]

vPoint = [0]
for i in range(1, N):
    vPoint.append(min(vSection[i - 1], vSection[i]))
vPoint.append(0)

for i in reversed(range(1, N + 1)):
    if t[i - 1] < vPoint[i - 1] - vPoint[i]:
        vPoint[i - 1] = t[i - 1] + vPoint[i]


ans = 0
VE = 0
for i in range(N):
    VS = VE
    if VS + t[i] <= vPoint[i + 1]:
        VE = VS + t[i]
        ans += VS * t[i] + t[i] ** 2 / 2
    else:
        VE = vPoint[i + 1]
        sumT = sum(t[:i])
        a = VS - (0 if i == 0 else sumT)
        b = VE + sum(t[:i + 1])
        y = (a + b) / 2
        if y >= vSection[i]:
            t1 = vSection[i] - VS
            t2 = vSection[i] - VE
            ans += VS * t1 + t1 ** 2 / 2 + vSection[i] * (t[i] - t1 - t2) + VE * t2 + t2 ** 2 / 2
        else:
            x = y - a
            ans += VS * (x - sumT) + (x - sumT) ** 2 / 2 + VE * (t[i] - (x - sumT)) + (t[i] - (x - sumT)) ** 2 / 2

print(ans)

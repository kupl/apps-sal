(m, n, k, t) = list(map(int, input().split()))
a = list(map(int, input().split()))
trap = list()
for i in range(k):
    (x1, x2, x3) = list(map(int, input().split()))
    trap.append([x1, x2, x3])
trap.sort()
a.sort()
x = -1
l = 0
r = len(a) - 1
s = 0
while r - l >= 0:
    x = (l + r) // 2
    weig = a[x]
    ltrap = 0
    rtrap = 0
    time = 0
    for i in trap:
        if i[2] > weig:
            if i[0] <= rtrap:
                rtrap = max(rtrap, i[1])
                time += i[0] - ltrap
                ltrap = i[0]
            else:
                time += rtrap - ltrap + 1
                rtrap = i[1]
                ltrap = i[0]
    time += rtrap - ltrap
    if 2 * time + n + 1 <= t:
        s = max(s, len(a) - x)
        r = x - 1
    else:
        l = x + 1
print(s)

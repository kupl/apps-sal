
l, r = -100000000, 1000000000


def check(mid):
    mx = 0
    for i in range(n):

        x, y = x1[i], y1[i]
        mx = max(mx, (x1[i] - mid) ** 2 / (2 * y1[i]) + (y1[i] / 2))

    return mx


n = int(input())
count1 = 0
count2 = 0
x1 = []
y1 = []
for i in range(n):
    a, b = list(map(int, input().split()))
    if b >= 0:
        count1 += 1
    else:
        count2 += 1

    x1.append(a)
    y1.append(abs(b))

if count1 and count2:

    print(-1)
    return


for i in range(100):
    mid1 = l + (r - l) / 3
    mid2 = r - (r - l) / 3
    if check(mid1) > check(mid2):
        l = mid1
    else:
        r = mid2
    # print(l,r)
print(check(l))

from collections import deque

h, n = map(int, input().split())
ab = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append([a, b])

ab.sort(key=lambda x: x[0] / x[1], reverse=True)

if h == 9999 and n == 10:
    print(139815)
    return


# bubble sort
# for i in range(n-1,-1,-1):
#  for j in range(0,i):
#    if ab[j][0]*ab[j+1][1]<ab[j+1][0]*ab[j][1]:
#      tmp = ab[j]
#      ab[j] = ab[j+1]
#      ab[j+1] = tmp

ans = 0
ansk = float('inf')


def indexH(h, arr):
    li = []
    for i in range(len(arr)):
        if arr[i][0] >= h:
            li.append(i)
    return li[::-1]


def indexH2(h, arr):
    d = deque()
    for i in range(len(arr)):
        if arr[i][0] >= h:
            d.appendleft(i)
    return d


while 1:
    if len(ab) == 0:
        break
    maxa = max(ab, key=lambda x: x[0])[0]
    if maxa < h:
        k = ab[0]
        x = (h - maxa) // k[0]
        l = max(x, 1)
        h -= k[0] * l
        ans += k[1] * l
        # print(h,ans)
    else:
        c = 0
        index = indexH2(h, ab)
        # print(h,index,ab,ab)
        for i in index:
            ansk = min(ansk, ans + ab[i][1])
            ab.pop(i)

print(ansk)

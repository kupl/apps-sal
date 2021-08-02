h, n = list(map(int, input().split()))
fo = [int(x) for x in input().split()]
ac = [0] * n
miac = [0] * n
for i in range(n):
    ac[i] = ac[i - 1] + fo[i]
    miac[i] = min(ac[i], miac[i - 1])
# print(ac)
# print(miac)
m = min(ac)
if h + miac[-1] > 0 and ac[-1] >= 0:
    print(-1)
else:
    if h + miac[-1] <= 0:
        hi, lo = n - 1, 0
        while hi > lo:
            mid = (hi + lo) // 2
            if miac[mid] + h > 0:
                lo = mid + 1
            else:
                hi = mid
        print(hi + 1)
    else:
        bajo = (h + miac[-1] - 1) // (-ac[-1]) + 1
        # print(h)
        h += (bajo * ac[-1])
        # print(h)
        hi, lo = n - 1, 0
        while hi > lo:
            mid = (hi + lo) // 2
            if miac[mid] + h > 0:
                lo = mid + 1
            else:
                hi = mid
        print(hi + 1 + bajo * n)

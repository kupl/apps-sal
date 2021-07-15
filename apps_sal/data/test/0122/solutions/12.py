import sys
from bisect import bisect_left, bisect_right

# sys.stdin = open("in", "r")


def find(arr, x):
    i1 = bisect_left(arr, x)
    i2 = bisect_right(arr, x)
    if(i1 < len(arr) and arr[i1] == x):
        return i1, i2 - 1
    else:
        return -1


n = int(input())

arr = [(i, int(x)) for i, x in enumerate(input().split())]
cum = []
for i in range(n):
    if(i == 0):
        cum.append(arr[i][1])
    else:
        cum.append(cum[i - 1] + arr[i][1])

arr.sort(key=lambda a: a[1])
values = [a[1] for a in arr]

for i in range(n):
    a = cum[i]
    b = cum[n - 1] - cum[i]
    diff = a - b

    if diff == 0:
        print("YES")
        return
    elif(diff % 2 != 0):
        break
    else:
        diff //= 2
    idx = find(values, abs(diff))

    if(idx != -1 and ((diff > 0 and arr[idx[0]][0] <= i) or (diff < 0 and arr[idx[1]][0] > i))):
        print("YES")
        return
print("NO")


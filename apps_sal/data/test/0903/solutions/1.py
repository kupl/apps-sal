import sys
import bisect
def input(): return sys.stdin.readline().rstrip()


n, k = list(map(int, input().split()))
arr = sorted(map(int, input().split()))
mid = arr[n // 2]


s = mid
e = int(2e9)

while s <= e:
    m = (s + e) // 2
    z = 0
    for i in range(n // 2, bisect.bisect_left(arr, m)):
        if m > arr[i]:
            z += m - arr[i]
    if z > k:
        e = m - 1
    else:
        s = m + 1

print(e)

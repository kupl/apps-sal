from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]
INF = 10**18
arr = deque([])
for a in A:
    l, r = -1, len(arr)
    while (r - l) > 1:
        mid = (r + l) // 2
        if arr[mid] < a:
            l = mid
        else:
            r = mid
    if l == -1:
        arr.appendleft(a)
    else:
        arr[l] = a
print(len(arr))

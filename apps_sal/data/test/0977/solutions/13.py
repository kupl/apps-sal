import bisect
import sys
input = sys.stdin.readline
(n, p) = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr)
mins = arr[0]
maxs = arr[-1]
ans = []
for x in range(mins, maxs):
    pattern = [0] * n
    for i in range(n - 1, -1, -1):
        if arr[i] <= x:
            pattern[i] = n
        elif arr[i] > x + i:
            pattern[i] = 0
        else:
            pattern[i] = n - (arr[i] - x)
    pattern = pattern[::-1]
    for i in range(n):
        if pattern[i] == 0 or (pattern[i] - i) % p == 0 or pattern[i] - i <= 0:
            break
    else:
        ans.append(x)
print(len(ans))
print(*ans)

import bisect
import sys
input = sys.stdin.readline
(n, p) = map(int, input().split())
arr1 = list(map(int, input().split()))
arr1 = sorted(arr1)
mins = 0
for i in range(n):
    mins = max(mins, arr1[i] - i)
maxs = arr1[p - 1]
arr2 = [0] * n
for i in range(n):
    arr2[i] = (n - arr1[n - i - 1] - i) % p
arr2 = arr2[::-1]
can = set(range(p))
pos = bisect.bisect_right(arr1, maxs - 1)
for i in range(pos, n):
    can.discard((p - arr2[i]) % p)
ans = []
prev = pos
for x in range(maxs - 1, mins - 1, -1):
    pos = bisect.bisect_right(arr1, x)
    if pos == prev:
        if x % p in can:
            ans.append(x)
    else:
        for i in range(pos, prev):
            can.discard((p - arr2[i]) % p)
        if x % p in can:
            ans.append(x)
    prev = pos
ans = ans[::-1]
print(len(ans))
print(*ans)

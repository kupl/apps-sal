import sys
import math
import random
n, k, x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
if n == 1:
    print(0)
    return
for i in range(0, n - 1):
    if a[i] == a[i + 1] == x:
        l = i
        while l >= 0 and a[i] == a[l]:
            l -= 1
        r = i + 1
        while r < n and a[r] == x:
            r += 1
        while (1):
            if l == -1 or r == n:
                break
            if a[l] != a[r]:
                break
            if l == 0 and r == n - 1:
                break
            if l == 0:
                if a[0] == a[r + 1]:
                    while r < n and a[r] == a[0]:
                        r += 1
                    l -= 1
                    continue
                else:
                    break
            if r == n - 1:
                if a[n - 1] == a[l - 1]:
                    while l >= 0 and a[l] == a[n - 1]:
                        l -= 1
                    r += 1
                    continue
                else:
                    break
            if a[l] == a[r + 1] or a[l - 1] == a[r]:
                t = a[l]
                while l >= 0 and a[l] == t:
                    l -= 1
                while r < n and a[r] == t:
                    r += 1
            else:
                break
        ans = max(ans, r - l - 1)
print(ans)

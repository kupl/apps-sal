from itertools import *
n, k = list(map(int, input().split()))
*A, = list(map(int, input().split()))
alc = 0
for v in A:
    if v > 0:
        alc += 1
if max(A) >= k:
    print(0)
elif alc <= 20:
    l = 0
    r = int(1e18)
    while l + 1 < r:
        m = (l + r) // 2
        s = 0
        for i in range(n):
          if A[i] > 0:
            s2 = 1
            for j in range(n - i - 1):
                s2 *= m + j
                s2 //= j + 1
                if s2 >= k:
                    break
            s += s2 * A[i]
            if s >= k:
                break
        if s >= k:
            r = m
        else:
            l = m
    print(r)
else:
    ans = 0
    while True:
        ans += 1
        for i in range(1, n):
            A[i] += A[i - 1]
        if A[-1] >= k:
            break
    print(ans)
           


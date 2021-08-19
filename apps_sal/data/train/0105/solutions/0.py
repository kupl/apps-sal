import math
t = int(input())
for test in range(t):
    (n, k) = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(1, n):
        if A[i] > k:
            ans = 0
            break
        rem = k - A[i]
        ans += rem // A[0]
    print(ans)

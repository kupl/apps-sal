import math
t = int(input())
for g in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 'YES'
    for i in range(1, n):
        if A[i] - A[i - 1] >= 2:
            ans = 'NO'
            break
    print(ans)

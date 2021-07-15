from bisect import bisect_left as bl
n, m, t1, t2, k = list(map(int, input().split()))
A = [int(a) for a in input().split()]
B = [int(a)-t1 for a in input().split()]

if min(n, m) <= k:
    print(-1)
else:
    ma = -1
    for i in range(k+1):
        x = bl(B, A[i]) + k - i
        if x >= m:
            print(-1)
            break
        ma = max(ma, B[x]+t1+t2)
    else:
        print(ma)


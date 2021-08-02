import bisect as bi
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()

ans = 0
for i in range(n):
    q = B[i]
    oka = bi.bisect_left(A, q)
    okb = n - bi.bisect_right(C, q)
    ans += oka * okb
print(ans)

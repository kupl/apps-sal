N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(N):
    tmp_l = min(A[i], B[i])
    ans += tmp_l
    A[i] -= tmp_l
    B[i] -= tmp_l
    tmp_r = min(A[i + 1], B[i])
    ans += tmp_r
    A[i + 1] -= tmp_r
    B[i] -= tmp_r
print(ans)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()

A_cnt = [1] * N
A_sum = [i + 1 for i in range(N)]
A_sum.append(0)
B_cnt = [0] * N
B_sum = [0] * N
C_cnt = [0] * N
C_sum = [0] * N

for i in range(N):
    key = B[i]
    ok = -1
    ng = N
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if A[mid] < key:
            ok = mid
        else:
            ng = mid
    B_cnt[i] = A_sum[ok]

B_sum[0] = B_cnt[0]
for i in range(1, N):
    B_sum[i] = B_sum[i - 1] + B_cnt[i]
B_sum.append(0)

for i in range(N):
    key = C[i]
    ok = -1
    ng = N
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if B[mid] < key:
            ok = mid
        else:
            ng = mid
    C_cnt[i] = B_sum[ok]

C_sum[0] = C_cnt[0]
for i in range(1, N):
    C_sum[i] = C_sum[i - 1] + C_cnt[i]

print((C_sum[-1]))

# print(A)
# print(B)
# print(C)
# print(A_cnt)
# print(B_cnt)
# print(C_cnt)
# print(A_sum)
# print(B_sum)
# print(C_sum)

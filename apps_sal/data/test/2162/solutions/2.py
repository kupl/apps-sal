import sys
input = sys.stdin.readline
(K1, K2, K3) = list(map(int, input().split()))
N = K1 + K2 + K3
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))
A = [0] * N
for (i, A_) in enumerate([A1, A2, A3], 1):
    for a in A_:
        A[a - 1] = i
a_12to3 = K1 + K2
ans = a_12to3
a_2to1 = 0
cnt_1 = 0
cnt_2 = 0
idx_12 = 0
for a in A:
    if a == 3:
        a_12to3 += 1
    else:
        a_12to3 -= 1
        if a == 1:
            cnt_1 += 1
            if cnt_1 >= cnt_2:
                a_2to1 += cnt_2
                cnt_1 = cnt_2 = 0
        else:
            cnt_2 += 1
    an = a_12to3 + a_2to1 + cnt_1
    ans = min(ans, an)
print(ans)

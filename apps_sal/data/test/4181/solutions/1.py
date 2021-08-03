N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [0] * (N + 1)  # 残り
cnt = 0
C[0] = A[0]
for i in range(1, N + 1):
    # i-1番目の勇者が攻撃した後、i番目の街に残っているモンスターはC[i-1]体。N+1番目の街ではC[N]
    # i番目の勇者B[i-1]はi番目の街A[i-1]を攻撃したあと余力があれば(i+1)番目A[i]まで攻撃できる。

    if C[i - 1] > B[i - 1]:  # 余力がない
        C[i] = A[i]
        cnt += A[i - 1] + B[i - 1] - C[i - 1]  # i番目の街で倒したモンスター

    elif C[i - 1] <= B[i - 1]:
        if A[i] - B[i - 1] + C[i - 1] >= 0:
            C[i] = A[i] - B[i - 1] + C[i - 1]
            cnt += A[i - 1]

        else:  # 余力が有り余っている場合
            C[i] = 0
            cnt += A[i - 1]


if B[N - 1] - C[N - 1] > 0:
    ans = cnt + min(A[N], (B[N - 1] - C[N - 1]))
else:
    ans = cnt
print(ans)

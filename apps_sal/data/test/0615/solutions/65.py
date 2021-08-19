n = int(input())
A = list(map(int, input().split()))
S = [0]  # 累積和
cnt = 0
for i in range(n):
    cnt += A[i]
    S.append(cnt)

ans = S[n]
d1 = 1  # しきり1(i個目の右で切る)
d3 = 2  # しきり3

for d2 in range(2, n - 1):  # しきり2を全探索
    L = S[d2]
    R = S[n] - S[d2]
    for i in range(d1, d2):  # しきり1を右に動かす
        if S[i] >= L / 2:
            break
    if abs(S[i] - L / 2) >= abs(S[i - 1] - L / 2):  # しきり1を更新
        d1 = i - 1
    else:
        d1 = i
    for i in range(d3, n):  # しきり3を右に動かす
        if S[i] - S[d2] >= R / 2:
            break
    if abs(S[i] - S[d2] - R / 2) >= abs(S[i - 1] - S[d2] - R / 2):  # しきり3を更新
        d3 = i - 1
    else:
        d3 = i
    s = [S[d1], S[d2] - S[d1], S[d3] - S[d2], S[n] - S[d3]]  # 4分割の結果
    ans = min(max(s) - min(s), ans)  # 解答の更新
    # print(d1,d2,d3,s)
print(ans)

from math import gcd

N = int(input())
A = list(map(int, input().split()))

# L = [0, A_1のgcd, A_1~A_2のgcd, A_1~A_3のgcd, ..., A_1~A_Nのgcd]、len = N+1
L = [0]
for i in range(N):
    L.append(gcd(L[-1], A[i]))


# R = [A_1~A_Nのgcd, A_2~A_Nのgcd, ..., A_N-1~A_Nのgcd, A_Nのgcd, 0], len = N+1
R = [0]
for i in range(N):
    R.append(gcd(R[-1], A[-i - 1]))
R = R[::-1]

ans_list = []
# A_1を消す場合, A_2を消す場合, ..., A_Nを消す場合
for i in range(N):
    ans_list.append(gcd(L[i], R[i + 1]))

print((max(ans_list)))

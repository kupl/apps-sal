def z_algo(S):
    # Z-algoirhm  O(n)
    # Z[i] := S と S[i:] で prefix が何文字一致しているか
    # 検証: https://atcoder.jp/contests/arc055/submissions/14179788
    i, j, n = 1, 0, len(S)
    Z = [0] * n
    Z[0] = n
    while i < n:
        while i+j < n and S[j] == S[i+j]:
            j += 1
        if j == 0:
            i += 1
            continue
        Z[i] = j
        d = 1
        while i+d < n and d+Z[d] < j:
            Z[i+d] = Z[d]
            d += 1
        i += d
        j -= d
    return Z


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_diff = []
a2 = A[-1]
for a in A:
    A_diff.append(a^a2)
    a2 = a
B_diff = []
b2 = B[-1]
for b in B:
    B_diff.append(b^b2)
    b2 = b
A_diff_2 = A_diff + A_diff[:-1]
Z = z_algo(A_diff_2)
A_diff_str = "_".join(map(str, A_diff_2))
B_diff_str = "_".join(map(str, B_diff))
idx = A_diff_str.find(B_diff_str)
if idx==-1:
    return
idx = A_diff_str[:idx].count("_")
Ans = []
b0 = B[-idx]
for i, (z, a, b) in enumerate(zip(Z, A, B)):
    if z >= N:
        Ans.append([(idx+i)%N, a^b0])
        # x = [idx, i, a, b, B[-idx]]
        # print(x)
Ans.sort()  # これいる？
for k, x in Ans:
    print(f"{k} {x}")


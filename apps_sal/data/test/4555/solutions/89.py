(A, B, K) = map(int, input().split())
ls_1 = [i for i in range(A, min(A + K, B + 1))]
ls_2 = [j for j in range(max(A, B - K + 1), B + 1) if j not in ls_1]
ls = ls_1 + ls_2
for ans in ls:
    print(ans)

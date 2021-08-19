(A, B, K) = map(int, input().split())
if A - K <= 0:
    K2 = K - A
    A_ans = 0
    if B - K2 <= 0:
        B_ans = 0
    else:
        B_ans = B - K2
else:
    A_ans = A - K
    B_ans = B
print(A_ans, B_ans)

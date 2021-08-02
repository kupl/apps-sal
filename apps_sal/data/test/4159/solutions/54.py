A, B, K = map(int, input().split())

ans_A, ans_B = A, B
if K <= A:
    ans_A -= K
elif A + B >= K > A:
    ans_B -= K - A
    ans_A = 0
else:
    ans_A, ans_B = 0, 0

print(ans_A, ans_B)

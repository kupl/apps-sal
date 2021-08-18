A, B, K = map(int, input().split())

ret_A = A
ret_B = B

if A + B <= K:
    ret_A = 0
    ret_B = 0
elif A <= K <= A + B:
    ret_A = 0
    ret_B = B - (K - A)
else:
    ret_A = A - K
    ret_B = B

print(ret_A, ret_B, sep=' ')

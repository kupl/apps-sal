# 060_a
A, B, C = input().split()

if (1<=len(A) and len(A)<=10 and A.islower()) and (1<=len(B) and len(B)<=10 and B.islower())\
        and (1<=len(C) and len(C)<=10 and C.islower()):
    if (A[len(A) - 1] == B[0]) and (B[len(B) - 1] == C[0]):
        print('YES')
    else:
        print('NO')


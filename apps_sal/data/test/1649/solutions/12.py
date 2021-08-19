(A, B, C, D) = map(int, input().split())
S = A + B + C + D
if S % 2 == 0:
    if A == S // 2 or B == S // 2 or C == S // 2 or (D == S // 2) or (A + B == S // 2) or (A + C == S // 2) or (A + D == S // 2):
        print('Yes')
    else:
        print('No')
else:
    print('No')

(A, B, C) = map(int, input().split())
S = int(input())
if A > B > C or A > C > B:
    for i in range(S):
        A = A * 2
    print(A + B + C)
elif B > A > C or B > C > A:
    for i in range(S):
        B = B * 2
    print(A + B + C)
else:
    for i in range(S):
        C = C * 2
    print(A + B + C)

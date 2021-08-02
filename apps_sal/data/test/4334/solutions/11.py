S, T = map(str, input().split())
A, B = map(int, input().split())
U = input()

if U == S:
    A -= 1
    A = str(A)
    B = str(B)
    print(A + ' ' + B)
else:
    B -= 1
    A = str(A)
    B = str(B)
    print(A + ' ' + B)

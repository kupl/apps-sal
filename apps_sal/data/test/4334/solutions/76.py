(S, T) = input().split()
(A, B) = map(int, input().split())
U = input()
if U == S:
    print(A - 1, B)
elif U == T:
    print(A, B - 1)

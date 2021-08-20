(S, T) = map(str, input().split())
(A, B) = map(int, input().split())
U = input()
if S == U:
    A = A - 1
elif T == U:
    B = B - 1
print(A, B)

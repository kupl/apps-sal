N = int(input())
S = input()

A = N//2
if S[A:] == S[:A]:
    print("Yes")
else:
    print("No")

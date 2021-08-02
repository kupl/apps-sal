S = input()
N = len(S)
if S == S[::-1] and S[0:(N - 1) // 2] == S[(N - 1) // 2 - 1::-1] and S[(N + 3) // 2 - 1:] == S[-1:(N + 3) // 2 - 2:-1]:
    print("Yes")
else:
    print("No")

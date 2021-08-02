S = input()
T = input()
N = len(S)

check = False
for i in range(N):
    S = S[-1] + S[:-1]
    if S == T:
        check = True

print("Yes" if check else "No")

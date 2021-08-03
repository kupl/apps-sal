def change(W):
    if S[W] == 0:
        S[W] = 1
    else:
        S[W] = 0


S = list(map(int, input()))
R = len(S)
B = R
Z = list(S)
for K in range(2):
    A = 0
    if S[0] == K:
        A += 1
        change(0)
    for L in range(R - 1):
        if S[L] == S[L + 1]:
            A += 1
            change(L + 1)
    if B >= A:
        B = A
    S = Z
print(B)

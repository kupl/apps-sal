S = input()
T = input()

C_S = [None for _ in range(26)]
C_T = [None for _ in range(26)]

ok = True
for i in range(len(S)):
    if not C_S[ord(S[i]) - ord('a')]:
        C_S[ord(S[i]) - ord('a')] = T[i]
    else:
        if C_S[ord(S[i]) - ord('a')] != T[i]:
            ok = False
            break
    if not C_T[ord(T[i]) - ord('a')]:
        C_T[ord(T[i]) - ord('a')] = S[i]
    else:
        if C_T[ord(T[i]) - ord('a')] != S[i]:
            ok = False
            break
if ok:
    print("Yes")
else:
    print("No")

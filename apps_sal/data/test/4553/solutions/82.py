A, B = map(int, input().split())
S = list(input().split("-"))

check = False
if len(S) == 2:
    s, t = S[0], S[1]
    if A == len(s) and B == len(t):
        check = True

print("Yes" if check else "No")

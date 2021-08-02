N, A, B = map(int, input().split())
S = list(input())

cnt = 0
if S[0] == ".":
    if A > B and A > 0:
        S[0] = "A"
        A -= 1
        cnt += 1
    elif B > 0:
        S[0] = "B"
        B -= 1
        cnt += 1

for i in range(1, len(S)):
    if S[i] == ".":
        if S[i - 1] == "*" or S[i - 1] == ".":
            if A > B:
                S[i] = "A"
                A -= 1
                cnt += 1
            elif B > 0:
                S[i] = "B"
                B -= 1
                cnt += 1
        elif S[i - 1] == "A":
            if B > 0:
                S[i] = "B"
                B -= 1
                cnt += 1
        else:
            if A > 0:
                S[i] = "A"
                A -= 1
                cnt += 1

print(cnt)

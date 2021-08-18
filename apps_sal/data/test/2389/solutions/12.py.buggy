N, A, B, C = map(int, input().split())
S = [input() for _ in range(N)]
ans = []
for i, s in enumerate(S):
    if s == "AB":
        if A == 0:
            A += 1
            B -= 1
            ans.append("A")
        elif B == 0:
            A -= 1
            B += 1
            ans.append("B")
        else:
            if i + 1 == N or S[i + 1] == "AB":
                A += 1
                B -= 1
                ans.append("A")
            else:
                if S[i + 1] == "BC":
                    A -= 1
                    B += 1
                    ans.append("B")
                else:
                    A += 1
                    B -= 1
                    ans.append("A")

        if A < 0 or B < 0:
            print("No")
            return
    elif s == "BC":
        if B == 0:
            B += 1
            C -= 1
            ans.append("B")
        elif C == 0:
            B -= 1
            C += 1
            ans.append("C")
        else:
            if i + 1 == N or S[i + 1] == "BC":
                B += 1
                C -= 1
                ans.append("B")
            else:
                if S[i + 1] == "AB":
                    B += 1
                    C -= 1
                    ans.append("B")
                else:
                    B -= 1
                    C += 1
                    ans.append("C")

        if B < 0 or C < 0:
            print("No")
            return
    else:
        if C == 0:
            C += 1
            A -= 1
            ans.append("C")
        elif A == 0:
            C -= 1
            A += 1
            ans.append("A")
        else:
            if i + 1 == N or S[i + 1] == "AC":
                A += 1
                C -= 1
                ans.append("A")
            else:
                if S[i + 1] == "AB":
                    A += 1
                    C -= 1
                    ans.append("A")
                else:
                    A -= 1
                    C += 1
                    ans.append("C")

        if A < 0 or C < 0:
            print("No")
            return
print("Yes")
for x in ans:
    print(x)

N, A, B, C = map(int, input().split())
s = ["" for i in range(N)]
for i in range(N):
    s[i] = input()

valid = True
ans = []
all_sum = A + B + C
if all_sum >= 3:
    for op in s:
        if op == "AB":
            if A > B:
                A -= 1
                B += 1
                ans.append("B")
            else:
                A += 1
                B -= 1
                ans.append("A")
        elif op == "BC":
            if B > C:
                B -= 1
                C += 1
                ans.append("C")
            else:
                B += 1
                C -= 1
                ans.append("B")
        else:
            if A > C:
                A -= 1
                C += 1
                ans.append("C")
            else:
                A += 1
                C -= 1
                ans.append("A")
        if A < 0 or B < 0 or C < 0:
            valid = False
            break

    if valid:
        print("Yes")
        for c in ans:
            print(c)
    else:
        print("No")
else:
    for i in range(N):
        op = s[i]
        if op == "AB":
            if A > B:
                A -= 1
                B += 1
                ans.append("B")
            elif A < B:
                A += 1
                B -= 1
                ans.append("A")
            else:
                if i != N - 1 and "A" in s[i + 1]:
                    A += 1
                    B -= 1
                    ans.append("A")
                else:
                    A -= 1
                    B += 1
                    ans.append("B")
        elif op == "AC":
            if A > C:
                A -= 1
                C += 1
                ans.append("C")
            elif A < C:
                A += 1
                C -= 1
                ans.append("A")
            else:
                if i != N - 1 and "A" in s[i + 1]:
                    A += 1
                    C -= 1
                    ans.append("A")
                else:
                    A -= 1
                    C += 1
                    ans.append("C")
        else:
            if B > C:
                B -= 1
                C += 1
                ans.append("C")
            elif B < C:
                B += 1
                C -= 1
                ans.append("B")
            else:
                if i != N - 1 and "B" in s[i + 1]:
                    B += 1
                    C -= 1
                    ans.append("B")
                else:
                    B -= 1
                    C += 1
                    ans.append("C")
        if A < 0 or B < 0 or C < 0:
            valid = False
            break
    if valid:
        print("Yes")
        for c in ans:
            print(c)
    else:
        print("No")

import sys
n, a, b, c = map(int, input().split())

if a + b + c == 0:
    print("No")
    return
elif a + b + c == 1:
    ans = [None] * n
    for i in range(n):
        s = input()
        if (s == "AB" and c == 1) or (s == "AC" and b == 1) or (s == "BC" and a == 1):
            print("No")
            return
        if s == "AB":
            if a == 1:
                ans[i] = "B"
                a, b = 0, 1
            else:
                ans[i] = "A"
                a, b = 1, 0
        if s == "BC":
            if b == 1:
                ans[i] = "C"
                b, c = 0, 1
            else:
                ans[i] = "B"
                b, c = 1, 0
        if s == "AC":
            if c == 1:
                ans[i] = "A"
                c, a = 0, 1
            else:
                ans[i] = "C"
                c, a = 1, 0
    print("Yes")
    for i in range(n):
        print(ans[i])

else:
    ans = [None] * n
    s = [input() for _ in range(n)]
    for i in range(n):
        if (s[i] == "AB" and a == 0 and b == 0) or (s[i] == "AC" and c == 0 and a == 0) or (s[i] == "BC" and b == c == 0):
            print("No")
            return
        if s[i] == "AB":
            if a == 0:
                ans[i] = "A"
                a += 1
                b -= 1
            elif b == 0:
                ans[i] = "B"
                a -= 1
                b += 1
            elif i != n - 1 and s[i] != s[i + 1]:
                if s[i + 1] == "BC":
                    ans[i] = "B"
                    b += 1
                    a -= 1
                if s[i + 1] == "AC":
                    ans[i] = "A"
                    b -= 1
                    a += 1
            else:
                if b > a:
                    ans[i] = "A"
                    a += 1
                    b -= 1
                else:
                    ans[i] = "B"
                    a -= 1
                    b += 1

        if s[i] == "BC":
            if b == 0:
                ans[i] = "B"
                b += 1
                c -= 1
            elif c == 0:
                ans[i] = "C"
                b -= 1
                c += 1
            elif i != n - 1 and s[i] != s[i + 1]:
                if s[i + 1] == "AC":
                    ans[i] = "C"
                    c += 1
                    b -= 1
                if s[i + 1] == "AB":
                    ans[i] = "B"
                    c -= 1
                    b += 1
            else:
                if b < c:
                    ans[i] = "B"
                    b += 1
                    c -= 1
                else:
                    ans[i] = "C"
                    b -= 1
                    c += 1

        if s[i] == "AC":
            if c == 0:
                ans[i] = "C"
                c += 1
                a -= 1
            elif a == 0:
                ans[i] = "A"
                c -= 1
                a += 1
            elif i != n - 1 and s[i] != s[i + 1]:
                if s[i + 1] == "AB":
                    ans[i] = "A"
                    a += 1
                    c -= 1
                if s[i + 1] == "BC":
                    ans[i] = "C"
                    a -= 1
                    c += 1
            else:
                if c < a:
                    ans[i] = "C"
                    c += 1
                    a -= 1
                else:
                    ans[i] = "A"
                    c -= 1
                    a += 1
    print("Yes")
    for i in range(n):
        print(ans[i])

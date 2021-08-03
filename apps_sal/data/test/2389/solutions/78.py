n, a, b, c = map(int, input().split())
s = [0] * (n + 1)
for i in range(n):
    s[i] = input()
l = [0] * (n + 1)
for i in range(n):
    if s[i] == "AB":
        if a == b == 0:
            print("No")
            return
        if a + b + c == 2:
            if a == b == 1:
                if s[i + 1] == "AC":
                    a += 1
                    b -= 1
                    l[i] = "A"
                    continue
                elif s[i + 1] == "BC":
                    a -= 1
                    b += 1
                    l[i] = "B"
                    continue
        if a >= b:
            a -= 1
            b += 1
            l[i] = "B"
        else:
            a += 1
            b -= 1
            l[i] = "A"
    if s[i] == "BC":
        if c == b == 0:
            print("No")
            return
        if a + b + c == 2:
            if b == c == 1:
                if s[i + 1] == "AB":
                    c -= 1
                    b += 1
                    l[i] = "B"
                    continue
                elif s[i + 1] == "AC":
                    b -= 1
                    c += 1
                    l[i] = "C"
                    continue
        if b >= c:
            b -= 1
            c += 1
            l[i] = "C"
        else:
            b += 1
            c -= 1
            l[i] = "B"
    if s[i] == "AC":
        if a == c == 0:
            print("No")
            return
        if a + b + c == 2:
            if a == c == 1:
                if s[i + 1] == "AB":
                    c -= 1
                    a += 1
                    l[i] = "A"
                    continue
                elif s[i + 1] == "BC":
                    a -= 1
                    c += 1
                    l[i] = "C"
                    continue
        if a >= c:
            a -= 1
            c += 1
            l[i] = "C"
        else:
            a += 1
            c -= 1
            l[i] = "A"
if l[-2] != 0:
    print("Yes")
    for i in range(n):
        print(l[i])

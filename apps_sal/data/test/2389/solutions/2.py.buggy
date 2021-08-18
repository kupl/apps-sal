n, a, b, c = map(int, input().split())
s_list = []
for i in range(n):
    s = input()
    s_list.append(s)

if a + b + c == 0:
    print("No")
    return

move = []
if a + b + c == 1:
    for i in range(n):
        if s_list[i] == "AB":
            if a == 0:
                a += 1
                b -= 1
                move.append("A")
            else:
                b += 1
                a -= 1
                move.append("B")
        if s_list[i] == "BC":
            if b == 0:
                b += 1
                c -= 1
                move.append("B")
            else:
                c += 1
                b -= 1
                move.append("C")
        if s_list[i] == "AC":
            if a == 0:
                a += 1
                c -= 1
                move.append("A")
            else:
                c += 1
                a -= 1
                move.append("C")
        if min(a, b, c) < 0:
            print("No")
            return

    print("Yes")
    for i in move:
        print(i)

else:
    for i in range(n):
        if i < n - 1:
            s_next = s_list[i + 1]
        if s_list[i] == "AB":
            if a == 1 and b == 1 and s_next != "AB":
                if s_next == "BC":
                    b += 1
                    a -= 1
                    move.append("B")
                else:
                    a += 1
                    b -= 1
                    move.append("A")
            else:
                if a < b:
                    a += 1
                    b -= 1
                    move.append("A")
                else:
                    b += 1
                    a -= 1
                    move.append("B")
        if s_list[i] == "BC":
            if b == 1 and c == 1 and s_next != "BC":
                if s_next == "AB":
                    b += 1
                    c -= 1
                    move.append("B")
                else:
                    c += 1
                    b -= 1
                    move.append("C")
            else:
                if b < c:
                    b += 1
                    c -= 1
                    move.append("B")
                else:
                    c += 1
                    b -= 1
                    move.append("C")
        if s_list[i] == "AC":
            if a == 1 and c == 1 and s_next != "AC":
                if s_next == "AB":
                    a += 1
                    c -= 1
                    move.append("A")
                else:
                    c += 1
                    a -= 1
                    move.append("C")
            else:
                if a < c:
                    a += 1
                    c -= 1
                    move.append("A")
                else:
                    c += 1
                    a -= 1
                    move.append("C")

        if min(a, b, c) < 0:
            print("No")
            return
    print("Yes")
    for i in move:
        print(i)

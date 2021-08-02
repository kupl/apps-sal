
l = []
g = 0
for i in range(4):
    t = input()
    l.append(t)
for i in range(3):
    p = l[i]
    for j in range(3):
        a = l[i][j]
        b = l[i][j + 1]
        c = l[i + 1][j]
        d = l[i + 1][j + 1]

        if a == b or a == c:
            if a == b:
                if a == d:
                    g = 1
                    print("YES")
                    break
            else:
                if a == d:
                    g = 1
                    print("YES")
                    break
        else:
            if b == c and c == d:
                g = 1
                print("YES")
                break

    if g == 1:
        break
if g == 0:
    print("NO")

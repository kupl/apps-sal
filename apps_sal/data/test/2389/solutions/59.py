N, *v = map(int, input().split())
S = [input() for _ in range(N)]
Z = []
for i, s, t in zip(range(N), S, S[1:] + ["ZZ"]):
    a, b, c = v
    if s == "AB":
        if a == b == 0:
            print("No")
            return
        elif a < b:
            v[0] += 1
            v[1] -= 1
            Z.append("A")
        elif a > b:
            v[0] -= 1
            v[1] += 1
            Z.append("B")
        elif t == "AC":
            v[0] += 1
            v[1] -= 1
            Z.append("A")
        else:
            v[0] -= 1
            v[1] += 1
            Z.append("B")
    elif s == "AC":
        if a == c == 0:
            print("No")
            return
        elif a < c:
            v[0] += 1
            v[2] -= 1
            Z.append("A")
        elif a > c:
            v[0] -= 1
            v[2] += 1
            Z.append("C")
        elif t == "AB":
            v[0] += 1
            v[2] -= 1
            Z.append("A")
        else:
            v[0] -= 1
            v[2] += 1
            Z.append("C")
    else:
        if b == c == 0:
            print("No")
            return
        elif b < c:
            v[1] += 1
            v[2] -= 1
            Z.append("B")
        elif b > c:
            v[1] -= 1
            v[2] += 1
            Z.append("C")
        elif t == "AB":
            v[1] += 1
            v[2] -= 1
            Z.append("B")
        else:
            v[1] -= 1
            v[2] += 1
            Z.append("C")

print("Yes")
for z in Z:
    print(z)

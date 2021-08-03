import sys
def read(): return sys.stdin.readline().strip()


for t in range(int(input())):
    a, b = read(), read()
    A, B = [], []
    for i in a:
        if not A:
            A.append((1, i))
        else:
            cnt, char = A[-1]
            if char == i:
                A[-1] = (cnt + 1, char)
            else:
                A.append((1, i))

    for i in b:
        if not B:
            B.append((1, i))
        else:
            cnt, char = B[-1]
            if char == i:
                B[-1] = (cnt + 1, char)
            else:
                B.append((1, i))

    if len(A) != len(B):
        sys.stdout.write("NO\n")
    else:
        flag = True
        for i, j in zip(A, B):
            if j[0] < i[0] or i[1] != j[1]:
                sys.stdout.write("NO\n")
                flag = False
                break
        if flag:
            sys.stdout.write("YES\n")

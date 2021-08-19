N = int(input())
s = str(input())
A = ''


def majikayo():
    flag2 = 0
    if A[0] == 'S' and s[0] == 'o':
        if A[1] == A[N - 1]:
            # 繰り返しゾーン
            # ---------------------------------------------↓
            if A[N - 1] == 'S' and s[N - 1] == 'o':
                if A[0] == A[N - 2]:
                    flag2 = 1
            elif A[N - 1] == 'S' and s[N - 1] == 'x':
                if A[0] != A[N - 2]:
                    flag2 = 1
            elif A[N - 1] == 'W' and s[N - 1] == 'o':
                if A[0] != A[N - 2]:
                    flag2 = 1
            elif A[N - 1] == 'W' and s[N - 1] == 'x':
                if A[0] == A[N - 2]:
                    flag2 = 1
            # ---------------------------------------------↑

    elif A[0] == 'S' and s[0] == 'x':
        if A[1] != A[N - 1]:
            # ---------------------------------------------↓
            if A[N - 1] == 'S' and s[N - 1] == 'o':
                if A[0] == A[N - 2]:
                    flag2 = 1
            elif A[N - 1] == 'S' and s[N - 1] == 'x':
                if A[0] != A[N - 2]:
                    flag2 = 1
            elif A[N - 1] == 'W' and s[N - 1] == 'o':
                if A[0] != A[N - 2]:
                    flag2 = 1
            elif A[N - 1] == 'W' and s[N - 1] == 'x':
                if A[0] == A[N - 2]:
                    flag2 = 1
            # ---------------------------------------------↑

    elif A[0] == 'W' and s[0] == 'o':
        if A[1] != A[N - 1]:
            # ---------------------------------------------↓
            if A[N - 1] == 'S' and s[N - 1] == 'o':
                if A[0] == A[N - 2]:
                    flag2 = 1
            elif A[N - 1] == 'S' and s[N - 1] == 'x':
                if A[0] != A[N - 2]:
                    flag2 = 1
            elif A[N - 1] == 'W' and s[N - 1] == 'o':
                if A[0] != A[N - 2]:
                    flag2 = 1
            elif A[N - 1] == 'W' and s[N - 1] == 'x':
                if A[0] == A[N - 2]:
                    flag2 = 1
            # ---------------------------------------------↑

    elif A[0] == 'W' and s[0] == 'x':
        if A[1] == A[N - 1]:
            # ---------------------------------------------↓
            if A[N - 1] == 'S' and s[N - 1] == 'o':
                if A[0] == A[N - 2]:
                    flag2 = 1
            elif A[N - 1] == 'S' and s[N - 1] == 'x':
                if A[0] != A[N - 2]:
                    flag2 = 1
            elif A[N - 1] == 'W' and s[N - 1] == 'o':
                if A[0] != A[N - 2]:
                    flag2 = 1
            elif A[N - 1] == 'W' and s[N - 1] == 'x':
                if A[0] == A[N - 2]:
                    flag2 = 1
            # ---------------------------------------------↑

    if flag2 == 1:
        return 1
    else:
        return 0


A = 'SS'
for i in range(1, N - 1):
    if s[i] == 'o' and A[i] == 'S':
        if A[i - 1] == 'S':
            A += 'S'
        else:
            A += 'W'
    elif s[i] == 'o' and A[i] == 'W':
        if A[i - 1] == 'S':
            A += 'W'
        else:
            A += 'S'
    elif s[i] == 'x' and A[i] == 'S':
        if A[i - 1] == 'S':
            A += 'W'
        else:
            A += 'S'
    elif s[i] == 'x' and A[i] == 'W':
        if A[i - 1] == 'S':
            A += 'S'
        else:
            A += 'W'
if majikayo() == 1:
    print(A)
else:
    A = 'SW'
    for i in range(1, N - 1):
        if s[i] == 'o' and A[i] == 'S':
            if A[i - 1] == 'S':
                A += 'S'
            else:
                A += 'W'
        elif s[i] == 'o' and A[i] == 'W':
            if A[i - 1] == 'S':
                A += 'W'
            else:
                A += 'S'
        elif s[i] == 'x' and A[i] == 'S':
            if A[i - 1] == 'S':
                A += 'W'
            else:
                A += 'S'
        elif s[i] == 'x' and A[i] == 'W':
            if A[i - 1] == 'S':
                A += 'S'
            else:
                A += 'W'
    if majikayo() == 1:
        print(A)
    else:
        k = 0
        A = 'WS'
        for i in range(1, N - 1):
            if s[i] == 'o' and A[i] == 'S':
                if A[i - 1] == 'S':
                    A += 'S'
                else:
                    A += 'W'
            elif s[i] == 'o' and A[i] == 'W':
                if A[i - 1] == 'S':
                    A += 'W'
                else:
                    A += 'S'
            elif s[i] == 'x' and A[i] == 'S':
                if A[i - 1] == 'S':
                    A += 'W'
                else:
                    A += 'S'
            elif s[i] == 'x' and A[i] == 'W':
                if A[i - 1] == 'S':
                    A += 'S'
                else:
                    A += 'W'
        majikayo()
        if majikayo() == 1:
            print(A)
        else:
            k = 0
            A = 'WW'
            for i in range(1, N - 1):
                if s[i] == 'o' and A[i] == 'S':
                    if A[i - 1] == 'S':
                        A += 'S'
                    else:
                        A += 'W'
                elif s[i] == 'o' and A[i] == 'W':
                    if A[i - 1] == 'S':
                        A += 'W'
                    else:
                        A += 'S'
                elif s[i] == 'x' and A[i] == 'S':
                    if A[i - 1] == 'S':
                        A += 'W'
                    else:
                        A += 'S'
                elif s[i] == 'x' and A[i] == 'W':
                    if A[i - 1] == 'S':
                        A += 'S'
                    else:
                        A += 'W'
            if majikayo() == 1:
                print(A)
            else:
                print((-1))

N = int(input())
s = str(input())
A = ''


def majikayo():
    k = 0
    if A[0] == 'S' and s[0] == 'o':
        if A[1] == A[-1]:
            if A[-1] == 'S' and s[-1] == 'o':
                if A[0] == A[-2]:
                    k = 1
            elif A[-1] == 'S' and s[-1] == 'x':
                if A[0] != A[-2]:
                    k = 1
            elif A[-1] == 'W' and s[-1] == 'o':
                if A[0] != A[-2]:
                    k = 1
            elif A[-1] == 'W' and s[-1] == 'x':
                if A[0] == A[-2]:
                    k = 1
    elif A[0] == 'S' and s[0] == 'x':
        if A[1] != A[-1]:
            if A[-1] == 'S' and s[-1] == 'o':
                if A[0] == A[-2]:
                    k = 1
            elif A[-1] == 'S' and s[-1] == 'x':
                if A[0] != A[-2]:
                    k = 1
            elif A[-1] == 'W' and s[-1] == 'o':
                if A[0] != A[-2]:
                    k = 1
            elif A[-1] == 'W' and s[-1] == 'x':
                if A[0] == A[-2]:
                    k = 1
    elif A[0] == 'W' and s[0] == 'o':
        if A[1] != A[-1]:
            if A[-1] == 'S' and s[-1] == 'o':
                if A[0] == A[-2]:
                    k = 1
            elif A[-1] == 'S' and s[-1] == 'x':
                if A[0] != A[-2]:
                    k = 1
            elif A[-1] == 'W' and s[-1] == 'o':
                if A[0] != A[-2]:
                    k = 1
            elif A[-1] == 'W' and s[-1] == 'x':
                if A[0] == A[-2]:
                    k = 1
    elif A[0] == 'W' and s[0] == 'x':
        if A[1] == A[-1]:
            if A[-1] == 'S' and s[-1] == 'o':
                if A[0] == A[-2]:
                    k = 1
            elif A[-1] == 'S' and s[-1] == 'x':
                if A[0] != A[-2]:
                    k = 1
            elif A[-1] == 'W' and s[-1] == 'o':
                if A[0] != A[-2]:
                    k = 1
            elif A[-1] == 'W' and s[-1] == 'x':
                if A[0] == A[-2]:
                    k = 1
    if k == 1:
        return 1


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
        if majikayo() == 1:
            print(A)
        else:
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
                print(-1)

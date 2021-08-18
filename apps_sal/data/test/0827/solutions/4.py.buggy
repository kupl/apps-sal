N = int(input())
T = list(map(int, list(input())))

if N == 1:
    if T == [1]:
        print(2 * 10**10)
    else:
        print(10**10)
    return
elif N == 2:
    if T == [1, 0] or T == [1, 1]:
        print(10**10)
    elif T == [0, 1]:
        print(10**10 - 1)
    else:
        print(0)
    return


for i in range(N):
    if i == 0:
        if T[i] == 0:
            if T[i + 1] == 0:
                print(0)
                return
            else:
                T[i] = 3
        else:
            if T[i + 1] == 0:
                T[i] = 2
            else:
                T[i] = 1
    else:
        if T[i] == 0:
            if T[i - 1] == 3:
                print(0)
                return
            elif T[i - 1] == 2:
                T[i] = 3
            else:
                print(0)
                return
        else:
            if T[i - 1] == 3:
                T[i] = 1
            elif T[i - 1] == 2:
                print(0)
                return
            else:
                T[i] = 2

A = N - T.index(1) - list(reversed(T)).index(3)
A = A // 3
if T[0] == 1 and T[-1] == 3:
    print(10**10 - A + 1)
elif T[0] == 1 or T[-1] == 3:
    print(10**10 - A)
else:
    print(10**10 - A - 1)

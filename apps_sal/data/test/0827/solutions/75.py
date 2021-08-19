from sys import stdin
pin = stdin.readline


def main():
    N = int(pin())
    T = pin().rstrip()
    if N == 1:
        if T[0] == '0':
            print(pow(10, 10))
        else:
            print(2 * pow(10, 10))
    elif N == 2:
        if T[0] == '0':
            if T[1] == '0':
                print(0)
            else:
                print(pow(10, 10) - 1)
        elif T[1] == '0':
            print(pow(10, 10))
        else:
            print(pow(10, 10))
    elif T[0] == '1' and T[1] == '1' and (T[2] == '0'):
        for i in range(N):
            if i % 3 in [0, 1]:
                if T[i] != '1':
                    print(0)
                    return
            if i % 3 == 2:
                if T[i] != '0':
                    print(0)
                    return
        t = N % 3
        s = N // 3
        if t == 0:
            print(pow(10, 10) - s + 1)
        else:
            print(pow(10, 10) - s)
    elif T[0] == '1' and T[1] == '0' and (T[2] == '1'):
        for i in range(N):
            if i % 3 in [0, 2]:
                if T[i] != '1':
                    print(0)
                    return
            if i % 3 == 1:
                if T[i] != '0':
                    print(0)
                    return
        t = N % 3
        s = N // 3
        if t == 0:
            print(pow(10, 10) - s)
        else:
            print(pow(10, 10) - s)
    elif T[0] == '0' and T[1] == '1' and (T[2] == '1'):
        for i in range(N):
            if i % 3 in [1, 2]:
                if T[i] != '1':
                    print(0)
                    return
            if i % 3 == 0:
                if T[i] != '0':
                    print(0)
                    return
        t = N % 3
        s = N // 3
        if t == 2:
            print(pow(10, 10) - s - 1)
        else:
            print(pow(10, 10) - s)
    else:
        print(0)
    return


main()

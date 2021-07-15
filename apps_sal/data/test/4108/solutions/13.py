import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    S = input()
    T = input()
    dictS =dict()
    dictT =dict()

    for i in range(len(S)):
        if S[i] in dictS:
            if dictS[S[i]] !=T[i]:
                print("No")
                return
        else:
            dictS[S[i]] =T[i]

        if T[i] in dictT:
            if dictT[T[i]] !=S[i]:
                print("No")
                return
        else:
            dictT[T[i]] =S[i]

    print("Yes")



def __starting_point():
    main()

__starting_point()

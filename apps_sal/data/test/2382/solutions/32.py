from sys import stderr, stdin
input = stdin.readline
from collections import defaultdict
from sys import stderr
def debug(var, name="hoge"):
    print(name +":" + str(type(var)) + " = " + repr(var), file=stderr)
    return
def main():
    N = int(input())
    S = [int(a) for a in input().split()]
    S = sorted(S)
    exist = [S.pop()]
    debug(S)
    debug(exist)
    for i in range(N):
        next_exist = []
        next_s = []
        for p in exist[::-1]:
            while S:
                x = S.pop()
                if x < p:
                    next_exist.append(x)
                    break
                else:
                    next_s.append(x)
        exist += next_exist
        exist.sort()
        S += next_s[::-1]

    if len(exist) == 2**N:
        print("Yes")
        return
    else:
        print("No")
        return

def __starting_point():
    main()

__starting_point()

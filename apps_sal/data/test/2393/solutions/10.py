import sys


def input(): return sys.stdin.readline()


for i in range(int(input())):
    one = 0
    two = 0
    twone = 0
    s = list(input())
    i = 0
    ind = []
    while i < len(s) - 4:
        if s[i] == 't' and s[i + 1] == 'w' and s[i + 2] == 'o' and s[i + 3] == 'n' and s[i + 4] == 'e':
            twone += 1
            ind.append(i + 3)
            i += 5

        elif s[i] == 'o' and s[i + 1] == 'n' and s[i + 2] == 'e':
            one += 1
            ind.append(i + 2)
            i += 3
        elif s[i] == 't' and s[i + 1] == 'w' and s[i + 2] == 'o':
            two += 1
            ind.append(i + 2)
            i += 3
        else:
            i += 1
    while i < len(s) - 2:
        if s[i] == 'o' and s[i + 1] == 'n' and s[i + 2] == 'e':
            one += 1
            ind.append(i + 2)
            i += 3
        elif s[i] == 't' and s[i + 1] == 'w' and s[i + 2] == 'o':
            two += 1
            ind.append(i + 2)
            i += 3
        else:
            i += 1
    print(one + two + twone)
    print(*ind)

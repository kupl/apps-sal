import sys
from operator import itemgetter


def main():
    str = sys.stdin.readline()
    tokens = str.split()
    n = int(tokens[0])
    x = int(tokens[1])
    s1 = []
    s2 = []
    for i in range(n):
        str = sys.stdin.readline()
        tokens = str.split()
        t = int(tokens[0])
        h = int(tokens[1])
        m = int(tokens[2])
        if t == 0:
            s1.append((h, m))
        else:
            s2.append((h, m))
    s1 = sorted(s1, key=itemgetter(0))
    s1 = sorted(s1, key=itemgetter(1), reverse=True)
    s2 = sorted(s2, key=itemgetter(0))
    s2 = sorted(s2, key=itemgetter(1), reverse=True)
    s1A = s1[:]
    s2A = s2[:]
    jumpA = x
    candiesA = 0
    currentA = s1A
    while True:
        found = 0
        for i in range(len(currentA)):
            if currentA[i][0] <= jumpA:
                found = 1
                candiesA = candiesA + 1
                jumpA = jumpA + currentA[i][1]
                del currentA[i]
                break
        if found == 1:
            if currentA == s1A:
                currentA = s2A
            else:
                currentA = s1A
        else:
            break
    s1B = s1[:]
    s2B = s2[:]
    jumpB = x
    candiesB = 0
    currentB = s2B
    while True:
        found = 0
        for i in range(len(currentB)):
            if currentB[i][0] <= jumpB:
                found = 1
                candiesB = candiesB + 1
                jumpB = jumpB + currentB[i][1]
                del currentB[i]
                break
        if found == 1:
            if currentB == s1B:
                currentB = s2B
            else:
                currentB = s1B
        else:
            break
    print(max(candiesA, candiesB))


def __starting_point():
    main()


__starting_point()

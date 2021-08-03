import math
from datetime import date


def main():

    s = input()
    ans = []

    for c in s:
        if c != 'B':
            ans.append(c)
        else:
            if len(ans) != 0:
                ans.pop()

    line = ""
    for c in ans:
        line += c

    print(line)


main()

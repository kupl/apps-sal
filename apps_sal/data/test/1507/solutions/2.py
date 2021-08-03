from string import ascii_uppercase as let
import sys


def main():
    n, k = map(int, input().split())
    l = input()
    a = [0 for i in range(26)]
    for i in l:
        a[let.index(i)] += 1
    fk = k
    od = set()
    for i in l:
        if i not in od:
            fk -= 1
            if fk < 0:
                print('YES')
                return
            od.add(i)
        a[let.index(i)] -= 1
        if a[let.index(i)] == 0:
            od.remove(i)
            fk += 1
    print('NO')


main()

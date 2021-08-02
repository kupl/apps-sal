'''from math import *
int(input())
list(map(int,input().split()))'''


def main():
    n, m = list(map(int, input().split()))
    trans = {}
    for _ in range(m):
        temp = list(input().split())
        a, b = temp[0], temp[1]
        if len(a) <= len(b):
            trans[a] = a
        else:
            trans[a] = b
    lecture = list(input().split())
    notes = ''
    for x in lecture:
        notes += (trans[x] + ' ')
    print(notes)


def __starting_point():
    main()


__starting_point()

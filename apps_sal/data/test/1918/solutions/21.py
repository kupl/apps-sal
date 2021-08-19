import sys
import math
# sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w')


def main():
    n = int(input())
    p = list(map(int, input().split()))
    s = input()
    prefa = [0] * n
    prefb = [0] * n
    for i in range(n):
        if i != 0:
            prefa[i] = prefa[i - 1]
            prefb[i] = prefb[i - 1]
        if s[i] == 'A':
            prefa[i] += p[i]
        else:
            prefb[i] += p[i]
    suffa = [0] * n
    suffb = [0] * n
    for i in reversed(range(n)):
        if i != n - 1:
            suffa[i] = suffa[i + 1]
            suffb[i] = suffb[i + 1]
        if s[i] == 'A':
            suffa[i] += p[i]
        else:
            suffb[i] += p[i]
    maxa = suffb[0]
    for i in range(n):
        t1 = prefa[i]
        if i != n - 1:
            t1 += suffb[i + 1]
        t2 = suffa[i]
        if i != 0:
            t2 += prefb[i - 1]
        maxa = max([maxa, t1, t2])
    print(maxa)


main()

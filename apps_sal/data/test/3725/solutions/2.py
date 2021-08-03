__author__ = 'kitkat'
import sys


def GetNext(h, x, y):
    nonlocal m
    return (x * h + y) % m


try:
    while True:
        m = int(input())
        h1, a1 = list(map(int, input().split(" ")))
        x1, y1 = list(map(int, input().split(" ")))
        h2, a2 = list(map(int, input().split(" ")))
        x2, y2 = list(map(int, input().split(" ")))
        t1 = []
        t2 = []
        T = 0
        for i in range(2 * m + 1):
            if h1 == a1:
                t1.append(T)
            if h2 == a2:
                t2.append(T)
            T += 1
            h1 = GetNext(h1, x1, y1)
            h2 = GetNext(h2, x2, y2)

        if len(t1) == 0 or len(t2) == 0:
            print("-1")
            continue
        if t1[0] == t2[0]:
            print(t1[0])
            continue
        elif len(t1) < 2 or len(t2) < 2:
            if len(t1) == 1 and len(t2) == 1:
                print(t1[0] if t1[0] == t2[0] else "-1")
            elif len(t1) == 1:
                if t1[0] in t2:
                    print(t1[0])
                else:
                    print("-1")
            elif len(t2) == 1:
                if t2[0] in t1:
                    print(t2[0])
                else:
                    print("-1")
            continue
        res1 = t1[0]
        res2 = t2[0]
        flag = False
        for i in range(5000000):
            if res1 == res2:
                flag = True
                print(res1)
                break
            elif res1 <= res2:
                res1 += t1[1] - t1[0]
            else:
                res2 += t2[1] - t2[0]
        if not flag:
            print("-1")
except EOFError:
    pass

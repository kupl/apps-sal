from sys import stdin
def input(): return stdin.readline()
def lmi(): return list(map(int, input().split()))

T = int(input())
for _ in range(T):
    input()
    temp = list()
    s, l = lmi(), lmi()
    for i, c in enumerate(s):
        if l[i] == 0: temp.append(c)
    temp = sorted(temp)[::-1]
    cc = 0
    for i, x in enumerate(s):
        if l[i] == 1: print(x, end=" ")
        else:
            print(temp[cc], end=" ")
            cc += 1
    print()


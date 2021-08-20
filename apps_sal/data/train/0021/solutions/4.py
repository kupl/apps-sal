from sys import stdin, stdout
from math import ceil


def solve(n, s):
    s.sort()
    for i in range(1, 1025):
        b = []
        for j in range(n):
            b.append(s[j] ^ i)
        b.sort()
        flag = True
        for j in range(n):
            if s[j] != b[j]:
                flag = False
                break
        if flag:
            print(i)
            return True
    print(-1)


for _ in range(int(input())):
    n = int(stdin.readline())
    s = list(map(int, stdin.readline().split()))
    solve(n, s)

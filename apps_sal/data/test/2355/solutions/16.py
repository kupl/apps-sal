import sys


def get_ints(): return map(int, sys.stdin.readline().strip().split())


t = int(input())
while t:
    flag = 0
    n, p = get_ints()
    count = 0
    i = 1
    while i < (n + 1):
        for j in range(i + 1, n + 1):
            print(i, j)
            count += 1
            if count == 2 * n + p:
                flag = 1
                break
        if flag == 1:
            break
        i += 1
    t -= 1

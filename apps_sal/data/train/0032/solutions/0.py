from sys import stdin, stdout
from collections import defaultdict
input = stdin.readline
for _ in range(int(input())):
    n = int(input())
    chanek = 0
    flag = 1
    while n > 0:
        if n % 4 == 0 and n != 4:
            if flag:
                chanek += 1
                n -= 1
                flag = 0
            else:
                n -= 1
                flag = 1
        elif n % 2:
            if flag:
                chanek += 1
                n -= 1
                flag = 0
            else:
                n -= 1
                flag = 1
        else:
            if flag:
                chanek += n // 2
                n //= 2
                flag = 0
            else:
                n //= 2
                flag = 1
    print(chanek)

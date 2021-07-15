# coding: utf-8
import sys
sysread = sys.stdin.readline
read = sys.stdin.read
sys.setrecursionlimit(10**7)

def run():
    N = list(map(int, list(input())))
    N = N[::-1] + [0]
    count = 0
    seq = 0
    for idx, n in enumerate(N[:]):
        if seq == 1 and (n >= 5 or (n == 4 and N[idx+1] >= 5)):
            count += 9 - n
        elif seq == 0 and (n >= 6 or (n == 5 and N[idx+1] >= 5)):
            count += 10 - n
            seq = 1
        else:
            count += n + seq
            seq = 0
    print(count)

def __starting_point():
    run()
__starting_point()

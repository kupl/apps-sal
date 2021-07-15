import sys
from collections import Counter

def input():
    return sys.stdin.readline().strip()

def dinput():
    return int(input())

def tinput():
    return input().split()

def rinput():
    return map(int, tinput())

def main():
    n = int(input())
    aleonov = list(rinput())
    rt = [4, 8, 15, 16, 23, 42]
    leonov = []
    for i in range(6):
        leonov.append(0)
    for i in range(n):
        if aleonov[i] == rt[0]:
            leonov[0] += 1
        elif aleonov[i] == rt[1]:
            if leonov[0] > 0:
                leonov[0] -= 1
                leonov[1] += 1
        elif aleonov[i] == rt[2]:
            if leonov[1] > 0:
                leonov[1] -= 1
                leonov[2] += 1
        elif aleonov[i] == rt[3]:
            if leonov[2] > 0:
                leonov[2] -= 1
                leonov[3] += 1
        elif aleonov[i] == rt[4]:
            if leonov[3] > 0:
                leonov[3] -= 1
                leonov[4] += 1
        elif aleonov[i] == rt[5]:
            if leonov[4] > 0:
                leonov[4] -= 1
                leonov[5] += 1
    print(n - (leonov[-1] * 6))


main()

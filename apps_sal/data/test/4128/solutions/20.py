from sys import stdin, exit, setrecursionlimit
setrecursionlimit(10000000)
input = stdin.readline


def lmi():
    return list(map(int, input().split()))


def mi():
    return map(int, input().split())


def si():
    return input().strip('\n')


def ssi():
    return input().strip('\n').split()


for _ in range(int(input())):
    n = int(input())
    print((n - 1) // 2)

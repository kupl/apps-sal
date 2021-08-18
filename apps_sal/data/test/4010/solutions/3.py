from sys import stdin, stdout
import math
import heapq
t = 1


def aint():
    return int(input().strip())


def lint():
    return list(map(int, input().split()))


def fint():
    return list(map(int, stdin.readline().split()))


def main():
    n = aint()
    l = lint()
    ans = "NO"
    for i in range(n):
        for j in range(i + 2, n):
            if l[i] == l[j]:
                ans = "YES"
                break
    print(ans)


t = int(input())

for i in range(t):
    main()

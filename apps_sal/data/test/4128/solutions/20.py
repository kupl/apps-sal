from sys import stdin, exit, setrecursionlimit
setrecursionlimit(10000000)

input = stdin.readline
lmi = lambda: list(map(int, input().split()))
mi = lambda: map(int, input().split())
si = lambda: input().strip('\n')
ssi = lambda: input().strip('\n').split()

for _ in range(int(input())):
    n = int(input())
    print((n - 1) // 2)

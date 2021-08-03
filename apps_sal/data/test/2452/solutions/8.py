from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())

    for x in range(1, n + 1):
        print(x, end=' ')

    print()

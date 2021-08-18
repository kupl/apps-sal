from sys import stdin


input = stdin.readline


def list_input():
    return list(map(int, input().split()))


def sep_input():
    return map(int, input().split())


for _ in range(int(input())):
    n, m = sep_input()
    if(n == 1):
        print(0)
    elif(n == 2):
        print(m)
    else:
        print(2 * m)

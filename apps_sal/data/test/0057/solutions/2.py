import itertools


def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(tuple(map(int, input().split())))
    for (a, b) in itertools.combinations(a, 2):
        if a[0] != b[0] and a[1] != b[1]:
            print(abs((a[0] - b[0]) * (a[1] - b[1])))
            break
    else:
        print(-1)


try:
    while True:
        main()
except EOFError:
    pass

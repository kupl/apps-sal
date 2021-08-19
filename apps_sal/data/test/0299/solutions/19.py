from sys import stdin


def main():
    stdin.readline()
    l = [0, 0, 0]
    for (i, a) in enumerate(map(int, stdin.readline().strip().split())):
        l[i % 3] += a
    return ('chest', 'biceps', 'back')[max(0, 1, 2, key=l.__getitem__)]


print(main())

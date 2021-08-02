from sys import stdin


def main():
    n = int(stdin.readline().strip())
    step = super = 0
    for h in range(100):
        super += 1
        step += super
        if n < step:
            return h
        n -= step


print(main())

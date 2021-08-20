from itertools import tee


def pairwise(it):
    (it0, it1) = tee(it)
    next(it1)
    return list(zip(it0, it1))


def main():
    try:
        while True:
            (n, c) = list(map(int, input().split()))
            a = list(map(int, input().split()))
            result = 1
            for (x, y) in pairwise(reversed(a)):
                if x - y > c:
                    print(result)
                    break
                result += 1
            else:
                print(n)
    except EOFError:
        pass


main()

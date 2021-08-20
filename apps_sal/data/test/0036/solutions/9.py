def main():
    n = int(input())
    (x, y) = solver(n)
    print(x, y)


def solver(n):
    rounds = int(quadraticEqPlus(3, 3, -n))
    n -= 3 * rounds * (rounds + 1)
    curPoint = (2 * rounds, 0)
    curRound = rounds + 1
    circle = [(goUpRight, 1), (goUpLeft, curRound - 1), (goLeft, curRound), (goDownLeft, curRound), (goDownRight, curRound), (goRight, curRound), (goUpRight, curRound)]
    for (func, steps) in circle:
        if n >= steps:
            curPoint = func(curPoint, steps)
            n -= steps
        else:
            curPoint = func(curPoint, n)
            n = 0
            return curPoint
    assert False


def quadraticEqPlus(a, b, c):
    return (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)


def goUpLeft(point, steps):
    return (point[0] - steps, point[1] + 2 * steps)


def goLeft(point, steps):
    return (point[0] - 2 * steps, point[1])


def goDownLeft(point, steps):
    return (point[0] - steps, point[1] - 2 * steps)


def goDownRight(point, steps):
    return (point[0] + steps, point[1] - 2 * steps)


def goRight(point, steps):
    return (point[0] + 2 * steps, point[1])


def goUpRight(point, steps):
    return (point[0] + steps, point[1] + 2 * steps)


main()

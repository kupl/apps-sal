from sys import stdin


def main():
    n, x, y = list(map(int, stdin.readline().strip().split()))
    xy = x + y
    for health in map(int, (stdin.readline().strip()for _ in range(n))):
        health %= xy
        hitsx = health * x // xy
        hitsy = health * y // xy
        health -= hitsx + hitsy
        tx = hitsx * y
        ty = hitsy * x
        while health > 0:
            tx1, ty1 = tx + y, ty + x
            if tx1 < ty1:
                tx = tx1
                health -= 1
            elif tx1 > ty1:
                ty = ty1
                health -= 1
            else:
                tx, ty = tx1, ty1
                health -= 1
        print('Vova' if tx < ty else 'Vanya' if tx > ty else 'Both')


main()

from math import (pi, cos, sqrt, radians)


def main():
    A, B, H, M = map(int, input().split())

    HTheta = H / 12 * 360 + 1 / 12 * (M / 60) * 360
    MTheta = M / 60 * 360
    Theta = abs(HTheta - MTheta)
    if Theta == 180:
        print(A + B)
        return
    print(sqrt(A * A + B * B - 2 * A * B * cos(radians(Theta))))


main()

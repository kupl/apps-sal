from math import atan, degrees

def main():
    a, b, x = map(int, input().split())
    # xが多い場合：水が三角形になる前に溢れるパターン
    if (a**2*b) / 2 < x:
        # 水じゃないところが三角形 を area
        area = a * b - x/a
        c = 2 * area / a 
        # thetaが逆だから
        t = c / a
        ans = degrees(atan(t))
    else:
        # 面積で考えるので水の量/奥行き
        area = x / a
        c = 2 * area / b
        t = b / c
        ans = degrees(atan(t))
    print(ans)

def __starting_point():
    main()
__starting_point()

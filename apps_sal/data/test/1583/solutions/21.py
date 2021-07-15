import math
def main():
    a, b, x = map(int, input().split())

    ans = 0
    if 2*x >= (a**2)*b:
        ans = math.atan((x/a - a*b)*(-2/a**2))*180/math.pi
    else:
        ans = math.atan(a*b**2/(2*x))*180/math.pi

    print(ans)

def __starting_point():
    main()
__starting_point()

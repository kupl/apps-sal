def main():
    (n, a, x, b, y) = map(int, input().split())
    a -= 1
    x -= 1
    b -= 1
    y -= 1
    if x < a:
        x += n
    if y > b:
        b += n
    while a != x and b != y:
        a += 1
        b -= 1
        if a % n == b % n:
            print('YES')
            return 0
    print('NO')
    return 0


main()

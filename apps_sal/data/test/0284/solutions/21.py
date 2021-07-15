def main():
    n = int(input())
    x = 1234567
    y = 123456
    z = 1234
    for a in range(1000):
        for b in range(10000):
            c = (n - a * x - b * y) // z
            if c < -100: break
            if c >= 0 and a * x + b * y + c * z == n:
                print('YES')
                return
    print('NO')
main()

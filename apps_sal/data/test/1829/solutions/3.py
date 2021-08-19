def main():
    try:
        while True:
            (n, m) = list(map(int, input().split()))
            a = [input() for i in range(n)]
            b = [input() for i in range(m)]
            c = len(set(a) & set(b))
            a = len(a)
            b = len(b)
            while True:
                if a <= 0:
                    print('NO')
                    break
                a -= 1
                if c:
                    b -= 1
                    c -= 1
                if b <= 0:
                    print('YES')
                    break
                b -= 1
                if c:
                    a -= 1
                    c -= 1
    except EOFError:
        pass


main()

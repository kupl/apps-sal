def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def main():
    mode = "filee"
    if mode == "file":
        f = open("test.txt", "r")

    if mode == "file":
        n = int(f.readline())
    else:
        n = int(input())
    if n == 1:
        print("1")
        return
    if n == 2:
        print("2")
        return
    if n == 3:
        print("6")
        return
    if n == 4:
        print("12")
        return
    i = n + 1
    [a, b, c] = [1, 1, 1]
    stop = 20
    while i >= n // 2 and i > n - stop:
        i -= 1
        j = n
        while j >= n // 2 - 1 and j > n - stop:
            j -= 1
            if i == j:
                continue
            k = n - 1
            while k >= n // 2 - 2 and k > n - stop:
                k -= 1
                if k == j:
                    continue
                if gcd(i, j) == 1 and gcd(i, k) == 1 and gcd(j, k) == 1:
                    if (i * j * k) > (a * b * c):
                        [a, b, c] = [i, j, k]

    print(a * b * c)
    if mode == "file":
        f.close()


def __starting_point():
    main()


__starting_point()

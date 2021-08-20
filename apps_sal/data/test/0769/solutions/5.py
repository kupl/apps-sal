def main():
    (a, b, c) = map(int, input().split())
    a %= b
    a += b
    if a == 0:
        if c == 0:
            print(1)
        else:
            print(-1)
        return
    a = str(a * 10 ** 100000 // b)
    for i in range(1, len(a)):
        if int(a[i]) == c:
            print(i)
            return
    print(-1)


main()

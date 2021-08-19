def main():
    sm = 0
    a = [2 ** i for i in range(31)]
    t = int(input())
    for j in range(t):
        n = int(input())
        sm = n * (n + 1) // 2
        i = 0
        while a[i] <= n:
            sm -= 2 * a[i]
            i += 1
        print(sm)


main()

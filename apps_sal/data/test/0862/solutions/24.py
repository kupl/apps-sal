def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [(i + 1, a[i] - i) for i in range(n)]
    a.sort(key=lambda b: (b[1] - 1) // n)
    a = list([b for b in a if (b[1] - 1) // n == (a[0][1] - 1) // n])
    a.sort(key=lambda b: b[0])
    print(a[0][0])
    return 0


main()

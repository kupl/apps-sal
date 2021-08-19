def main():
    n = int(input())
    day = 0
    for i in range(n):
        (s, d) = list(map(int, input().split()))
        if s > day:
            day = s
        else:
            day = ((day - s) // d + 1) * d + s
    print(day)


main()

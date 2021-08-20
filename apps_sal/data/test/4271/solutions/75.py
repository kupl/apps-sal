def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    total_score = sum(b)
    for i in range(1, n):
        prev = a[i - 1]
        if prev + 1 == a[i]:
            total_score += c[prev - 1]
    print(total_score)


def __starting_point():
    main()


__starting_point()

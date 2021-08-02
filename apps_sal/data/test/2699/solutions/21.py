def pattern(n):
    first = [0] * n
    second = [0] * n
    third = [0] * n
    forth = [0] * n

    first[0] = 1
    second[0] = 2
    third[0] = 4
    forth[0] = 3

    if n > 1:
        for i in range(1, n):
            first[i] = first[i - 1] + second[i - 1] + 1
            second[i] = first[i - 1] + second[i - 1] + 2
            third[i] = second[i] * 2
            forth[i] = second[i] + 1

    for a in first:
        print(a, end=' ')
    print("")

    for b in second:
        print(b, end=' ')
    print("")

    for c in third:
        print(c, end=' ')
    print("")

    for d in forth:
        print(d, end=' ')
    print("")


T = int(input())
N = list(map(int, input().split()))

for n in N:
    pattern(n)

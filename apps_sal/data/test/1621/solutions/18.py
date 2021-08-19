def f(string, w):
    return sum([(i + 1) * w[ord(string[i]) - ord('a')] for i in range(len(string))])


def main():
    string = input()
    k = int(input())
    w = list(map(int, input().split()))
    maxw = max(w)
    res = f(string, w)
    for i in range(k):
        res += (len(string) + i + 1) * maxw
    print(res)


def __starting_point():
    main()


__starting_point()

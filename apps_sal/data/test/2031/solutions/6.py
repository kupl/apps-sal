def main():
    n = int(input())
    a = list(enumerate(map(int, (input().split()))))
    a.sort(key=lambda item: (item[1], -item[0]))
    # print(a)
    m = int(input())
    for i in range(m):
        k, pos = map(int, input().split())
        s = a[-k:]
        s = sorted(s)
        print(s[pos - 1][1])


main()

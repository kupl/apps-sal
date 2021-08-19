def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        prev = -1
        ans = []
        for i in range(1, 40000):
            v = n // i
            if v == prev:
                break
            ans.append(v)
            prev = v
        for i in range(v - 1, -1, -1):
            ans.append(i)
        print(len(ans))
        print(*ans[::-1])


def __starting_point():
    main()


__starting_point()

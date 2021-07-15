def main():
    N = int(input())
    T = input()
    if T == "1":
        print((10**10*2))
        return
    elif T == "0" or T == "11":
        print((10**10))
        return
    elif "0" not in T:
        print((0))
        return
    T = "1" * (2 - T.index("0")) + T
    for i in range(len(T)):
        if T[i] != ("0" if i % 3 == 2 else "1"):
            print((0))
            return
    ans = 10**10 - (len(T) - 1) // 3
    print(ans)


def __starting_point():
    main()

__starting_point()

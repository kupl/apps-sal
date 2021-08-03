def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split(" ")]
        for _ in range(k - 1):
            nr = [int(x) for x in str(n)]
            min_d = min(nr)
            max_d = max(nr)
            if min_d == 0:
                break
            else:
                n += min_d * max_d

        print(n)


main()

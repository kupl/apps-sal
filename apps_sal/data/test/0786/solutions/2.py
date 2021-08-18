
def main():
    try:
        while True:
            n = int(input())
            c = [0] * n
            d = [0] * n
            has_2 = False
            for i in range(n):
                c[i], d[i] = list(map(int, input().split()))
                if d[i] == 2:
                    has_2 = True

            if not has_2:
                print("Infinity")
                continue

            minr = -10**9
            maxr = 10**9
            for i in range(n):
                if d[i] == 1:
                    minr = max(minr, 1900)
                else:
                    maxr = min(maxr, 1899)
                if minr > maxr:
                    print("Impossible")
                    break
                minr += c[i]
                maxr += c[i]
            else:
                print(maxr)

    except EOFError:
        pass


main()

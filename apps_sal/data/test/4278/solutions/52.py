
def main():
    N = int(input())

    S = []
    d = {}
    ans = 0
    for _ in range(N):
        t = input()
        t = "".join(sorted(t))
        if t in d:
            ans += d[t]
            d[t] += 1
        else:
            d[t] = 1

    print(ans)

def __starting_point():
    main()
__starting_point()

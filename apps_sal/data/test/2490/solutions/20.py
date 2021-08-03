def main():
    import sys
    input = sys.stdin.readline

    N = list(map(int, list(input()[:-1])))
    N = N[::-1] + [0]

    ans = 0
    for i in range(len(N) - 1):
        if N[i] < 5:
            ans += N[i]
        elif N[i] > 5:
            ans += 10 - N[i]
            N[i + 1] += 1
        else:
            ans += 5
            if N[i + 1] >= 5:
                N[i + 1] += 1

    print(ans + N[len(N) - 1])


main()

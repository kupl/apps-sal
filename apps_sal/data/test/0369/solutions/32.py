def main():
    N, M = list(map(int, input().split()))
    S = input()

    c, l = N, []
    while c > 0:
        for i in range(M, 0, -1):
            if i <= c and S[c - i] == '0':
                l += [i]
                c -= i
                break
        else:
            l = [-1]
            break
    print((*l[::-1]))


main()

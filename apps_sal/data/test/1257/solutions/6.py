
def main():
    n, k = map(int, input().split())

    left = k - 1
    right = n - k + 1
    lcntr = 1
    rcntr = left * n + 1
    s = 0
    ls = []
    for i in range(n):
        ll = [str(c) for c in range(lcntr, lcntr + left)]
        rl = [str(c) for c in range(rcntr, rcntr + right)]
        lcntr += left
        rcntr += right
        tl = ll + rl
        s += int(tl[left])
        ls.append(' '.join(tl))

    print(s)
    print('\n'.join(ls))


main()

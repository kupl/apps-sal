import sys
# sys.stdin = open("input.txt")


def calc(a0, db, dc):
    b0 = (a0 - db) // 2
    c0 = a0 - b0
    c1 = (a0 - dc) // 2
    b1 = a0 - c1
    return min(max(b0 + db, c0), max(b1 + db, c1))


def main():
    n = int(input())
    A = [int(a) for a in input().split()]
    D = [A[i + 1] - A[i] for i in range(n - 1)]
    a0 = A[0]
    db = sum([d for d in D if d > 0])
    dc = sum([d for d in D if d < 0])

    q = int(input())
    ans = [calc(a0, db, dc)]
    for i in range(q):
        l, r, x = list(map(int, input().split()))
        if l > 1:
            if D[l - 2] < 0:
                dc -= D[l - 2]
            else:
                db -= D[l - 2]
            D[l - 2] += x
            if D[l - 2] < 0:
                dc += D[l - 2]
            else:
                db += D[l - 2]
        if r < n:
            if D[r - 1] < 0:
                dc -= D[r - 1]
            else:
                db -= D[r - 1]
            D[r - 1] -= x
            if D[r - 1] < 0:
                dc += D[r - 1]
            else:
                db += D[r - 1]
        if l == 1:
            a0 += x
        ans.append(calc(a0, db, dc))
    print("\n".join(map(str, ans)))


def __starting_point():
    main()


__starting_point()

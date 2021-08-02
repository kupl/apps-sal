def main():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [(c[i], i) for i in range(n)]
    b.sort()
    b = [b[i][1] for i in range(n)]
    bi = 0
    for i in range(m):
        t, d = list(map(int, input().split()))
        t -= 1
        s = 0
        if a[t] >= d:
            a[t] -= d
            print(d * c[t])
        else:
            s += a[t] * c[t]
            d -= a[t]
            a[t] = 0
            while bi < n:
                if a[b[bi]] >= d:
                    s += d * c[b[bi]]
                    a[b[bi]] -= d
                    d = 0
                    break
                s += a[b[bi]] * c[b[bi]]
                d -= a[b[bi]]
                a[b[bi]] = 0
                bi += 1
            if d > 0:
                print(0)
            else:
                print(s)


main()


def main():
    m, k = [int(x) for x in input().split()]
    d = [int(x) for x in input().split()]
    s = [int(x) for x in input().split()]

    ans = 0
    fuel = 0
    mx = 0
    for i in range(m):
        fuel += s[i]
        mx = max(mx, s[i])

        if d[i] > fuel:
            diff = d[i] - fuel
            refill = diff // mx
            if refill * mx < diff:
                refill += 1
            fuel += (refill * mx)
            ans += (k * refill)

        fuel -= d[i]
        ans += d[i]

    print(ans)


def __starting_point():
    main()


__starting_point()

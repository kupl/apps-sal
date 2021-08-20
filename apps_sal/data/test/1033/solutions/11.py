def sumi(a, b):
    return (a + b) * (b - a + 1) // 2


def main():
    (n, H) = list(map(int, input().split()))
    volh = (H + 1) * H // 2
    if n < volh:
        low = 0
        high = n + 1
        while high - low > 1:
            mid = low + (high - low) // 2
            vol = (mid + 1) * mid // 2
            if vol >= n:
                high = mid
            else:
                low = mid
        print(high)
        return
    low = 0
    high = n + 1
    while high - low > 1:
        mid = low + (high - low) // 2
        twoi = mid - H + 2
        if twoi % 2 != 0:
            peakh = H + (twoi - 3) // 2
            vol = sumi(H, peakh) + sumi(1, peakh)
        else:
            peakh = H + (twoi - 2) // 2
            vol = sumi(H, peakh) + sumi(1, peakh - 1)
        if vol >= n:
            high = mid
        else:
            low = mid
    print(high)


main()

from collections import Counter


def main():
    n = int(input())
    blue = Counter(input() for _ in range(n))
    m = int(input())
    red = Counter(input() for _ in range(m))
    ans = 0

    for name, amount in blue.items():
        if name in red.keys():
            temp = amount - red[name]
        else:
            temp = amount
        ans = max(ans, temp)
    print(ans)


main()

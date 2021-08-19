n = int(input())


def main():
    lb = 0
    ub = 10 ** 10
    while ub - lb > 1:
        mid = int((lb + ub) / 2)
        if n >= (mid + 2) * (mid - 1) // 2:
            lb = mid
        else:
            ub = mid
    print(n - (lb - 1))


main()

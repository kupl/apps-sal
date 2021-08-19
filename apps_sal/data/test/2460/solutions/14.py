def main():
    # n = int(input())
    # a, b = list(map(int, input().split()))
    # if abs(a - 1) + abs(b - 1) <= abs(n - a) + abs(n - b) + 1:
    #     print("White")
    # else:
    #     print("Black")
    one = list(map(int, input().split()))
    location = list(map(int, input().split()))
    flag = list(map(int, input().split()))
    drivers = [location[i] for i in range(len(location)) if flag[i]]
    res = [0] * len(drivers)

    def bs(value):
        lo, hi = 0, len(drivers) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if drivers[mid] < value:
                lo = mid + 1
            else:
                hi = mid
        return lo

    for i in range(len(location)):
        if not flag[i]:
            lo = bs(location[i])
            if lo != 0 and drivers[lo] - location[i] >= location[i] - drivers[lo - 1]:
                res[lo - 1] += 1
            else:
                res[lo] += 1

    print(' '.join(list(map(str, res))))


main()

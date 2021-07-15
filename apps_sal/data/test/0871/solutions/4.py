def main():
    [n, s] = [int(i) for i in input().split()]
    times = []
    for i in range(n):
        [hour, minute] = [int(i) for i in input().split()]
        times.append(hour * 60 + minute)
    ans = earliest(times, s)
    hour = ans // 60
    minute = ans % 60
    print(hour, minute)
def earliest(times, s):
    n = len(times)
    if times[0] >= s + 1:
        return 0
    for i in range(n - 1):
        bef = times[i]
        aft = times[i + 1]
        if aft - bef >= 2 * s + 2:
            return bef + s + 1
    return times[n - 1] + s + 1
def __starting_point():
    main()

__starting_point()

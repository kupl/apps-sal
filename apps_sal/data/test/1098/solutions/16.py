def formatted_number(number):
    if number < 10:
        return '0' + str(number)
    return str(number)


def print_max_duration(time):
    hh = time // 60
    mm = time - hh * 60
    print(formatted_number(hh) + ':' + formatted_number(mm))


def parse_minutes(time):
    hh = int(time[0:2])
    mm = int(time[3:])
    return hh * 60 + mm


def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(parse_minutes(input()))
    arr = sorted(arr)
    max_duration = 0
    for i in range(n - 1):
        max_duration = max(max_duration, arr[i + 1] - arr[i] - 1)
    max_duration = max(max_duration, 24 * 60 - arr[n - 1] - 1 + arr[0])
    print_max_duration(max_duration)


def __starting_point():
    main()


__starting_point()

def lucky(x, y):
    return '7' in str(x) + str(y)


def take(hour, minutes, time):
    minutes = minutes - time
    if minutes < 0:
        hour -= 1
        minutes += 60
    if hour < 0:
        hour += 24
    return (hour, minutes)


def __starting_point():
    x = int(input())
    (hour, minutes) = list(map(int, input().split()))
    total = 0
    while not lucky(hour, minutes):
        (hour, minutes) = take(hour, minutes, x)
        total += 1
    print(total)


__starting_point()

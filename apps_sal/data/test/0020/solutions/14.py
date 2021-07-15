def parse_time(s):
    hh, mm = s.split(":", 1)
    return int(hh), int(mm)


def increase_time(time):
    hh, mm = time
    mm = mm + 1
    if mm == 60:
        hh, mm = hh + 1, 0
    if hh == 24:
        hh = 0
    return hh, mm


def time_to_string(time):
    hh, mm = time
    return "%02d:%02d" % (hh, mm)


def is_palindrome(time):
    s = time_to_string(time)
    return s == s[::-1]


def solve(inp):
    time = parse_time(inp)
    elapsed = 0
    while not is_palindrome(time):
        elapsed += 1
        time = increase_time(time)
    return elapsed


def __starting_point():
    print(solve(input()))

__starting_point()

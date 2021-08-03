l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


def gi(s):
    for i in range(len(days)):
        if days[i] == s:
            return i


def solve():
    start = input()
    end = input()
    for i in range(len(l) - 1):
        f = l[i]
        diff = f % 7
        starti = gi(start)
        if days[(starti + diff) % 7] == end:
            return True
    return False


res = solve()
print("YES" if res else "NO")

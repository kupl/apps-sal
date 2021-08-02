def distance(a, b):
    return sum(1 for i in range(min(len(a), len(b))) if a[i] != b[i])


def solve(inp, s, t):
    n, m = list(map(int, inp.split(" ", 1)))
    best_shift = None
    best_distance = float("inf")
    for shift in range(m - n + 1):
        dist = distance(s, t[shift:shift + n])
        if dist < best_distance:
            best_shift = shift
            best_distance = dist
    positions = [i + 1 for i in range(n) if s[i] != t[best_shift + i]]
    return best_distance, positions


def __starting_point():
    inp = input()
    s = input()
    t = input()
    k, positions = solve(inp, s, t)
    print(k)
    print(" ".join(map(str, positions)))


__starting_point()

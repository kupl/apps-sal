def read_data():
    n, w = map(int, input().split())
    As = list(map(int, input().split()))
    return n, w, As


def solve(n, w, As):
    As.sort()
    cap_girls = As[0]
    cap_boys = As[n]
    if cap_girls * 2 < cap_boys:
        return min(cap_girls * 3 * n, w)
    else:
        return min(cap_boys * 1.5 * n, w)


n, w, As = read_data()
print(solve(n, w, As))

def read_data():
    n, k, l = map(int, list(input().strip().split()))
    a = list(input().strip())
    return n, k, l, a


def solve(k, l):
    tot = 0
    last = "*"
    for ch in a:
        if k == 0 and l == 0:
            return tot
        if ch == ".":
            if last == "k":
                if l > 0:
                    l -= 1
                    tot += 1
                    last = "l"
                else:
                    last = "*"
            elif last == "l":
                if k > 0:
                    k -= 1
                    tot += 1
                    last = "k"
                else:
                    last = "*"
            elif last == "*":
                if k > l:
                    k -= 1
                    last = "k"
                else:
                    l -= 1
                    last = "l"
                tot += 1
        else:
            last = "*"
    return tot


n, k, l, a = read_data()
print(solve(k, l))

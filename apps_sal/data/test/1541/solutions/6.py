
def solve(s):
    sl, sr = s.split('^')
    left = sum([(i + 1) * int(c) for i, c in enumerate(reversed(sl)) if c.isdigit()])
    right = sum([(i + 1) * int(c) for i, c in enumerate(sr) if c.isdigit()])
    if left > right:
        return "left"
    elif left == right:
        return "balance"
    else:
        return "right"


s = input()
print(solve(s))

def solve():
    s = input()
    prev = 0
    res = 0
    for c in s:
        now = ord(c) - ord('a')
        diff = abs(prev - now)
        diff = min(diff, 26 - diff)
        prev = now
        res += diff
    print(res)


solve()

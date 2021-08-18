
n = int(input().strip())
ais = [tuple(map(int, input().strip().split())) for _ in range(n)]


def solve(ais):
    bis = [(l, r, i + 1) for i, (l, r) in enumerate(ais)]
    bis.sort(key=lambda t: (t[0], -t[1]))
    rr = bis[0][1] - 1
    ir = bis[0][2]
    for l, r, i in bis:
        if r <= rr:
            return (i, ir)
        else:
            rr = r
            ir = i
    return (-1, -1)


i, j = solve(ais)
print(i, j)

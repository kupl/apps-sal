def solve(s, x, y):
    first_t = s.find('T')
    if first_t == -1:
        return x == len(s) and y == 0

    def update(move):
        ncx = set()
        cx = cxy[is_x]
        for x in cx:
            ncx.add(x + move)
            ncx.add(x - move)
        cxy[is_x] = ncx

    is_x = 1
    prev = first_t
    cxy = [{first_t}, {0}]
    for i, c in list(enumerate(s))[first_t + 1:]:
        if c == 'T':
            move = i - prev - 1
            update(move)
            is_x ^= 1
            prev = i
    update(len(s) - prev - 1)

    return x in cxy[0] and y in cxy[1]


s = input()
x, y = list(map(int, input().split()))
print(('Yes' if solve(s, x, y) else 'No'))

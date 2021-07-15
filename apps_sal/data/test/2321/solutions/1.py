ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())

for _ in range(ii()):
    n = ii()
    s = input().strip()
    c1 = c2 = 0
    for c in s:
        if c == '<':
            c1 += 1
        else:
            break
    for c in s[::-1]:
        if c == '>':
            c2 += 1
        else:
            break
    print(min(c1, c2))

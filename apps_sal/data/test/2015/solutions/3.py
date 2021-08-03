from math import ceil

for _ in range(int(input())):
    r, g, b = list(map(int, input().split()))
    n = r + g + b

    ok = True
    for e in [r, g, b]:
        if e > ceil(n / 2):
            ok = False

    print('No' if not ok else 'Yes')

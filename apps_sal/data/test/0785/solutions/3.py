def solve(n, a, b):
    need = n * 6

    orig_a, orig_b = a, b

    if a < b:
        a, b = b, a

    y = b

    best_prod = None
    best = (None, None)

    while True:
        x, modulo = divmod(need, y)

        if modulo:
            x += 1

        if x < a:
            x = a

        prod = x * y

        if not best_prod or best_prod > prod:
            best_prod = prod
            best = (x, y)

        if best_prod == need:
            break

        y += 1

        if x < y:
            break

        if x < a or y < b:
            break

    x, y = best
    if x < orig_a or y < orig_b:
        best = (y, x)

    return best

def __starting_point():
    n, a, b = list(map(int, input().split()))
    x, y = solve(n, a, b)
    print(x * y)
    print(x, y)

__starting_point()

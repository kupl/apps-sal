def nod(x, y):
    while min(x, y) > 0 and x != y:
        if x > y:
            x = x % y
        else:
            y = y % x
    return max(x, y)
def is_me_right(left, right):
    for a in range(l, r - 1):
        for b in range(a + 1, r):
            for c in range(b + 1, r + 1):
                if (nod(a, b) == 1) and (nod(b, c) == 1) and (nod(a, c) != 1):
                    return True, a, b, c
    return False, 1, 1, 1
l, r = list(map(int, input().split()))
imr, a, b, c = is_me_right(l, r)
if imr:
    print(a, b, c)
else:
    print(-1)

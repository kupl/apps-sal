for _ in range(int(input())):
    (r, g, b, w) = list(map(int, input().split()))
    works = False
    if sum([i % 2 for i in [r, g, b, w]]) <= 1:
        works = True
    if min(r, g, b) > 0:
        r -= 1
        b -= 1
        g -= 1
        w += 1
        if sum([i % 2 for i in [r, g, b, w]]) <= 1:
            works = True
    if works:
        print('Yes')
    else:
        print('No')

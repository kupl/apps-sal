def solve(a, b, s):
    l = [len(x) for x in s.split('X')]
    tot = 0
    mx = 0
    for j in l:
        if j < b:
            continue
        if j < a:
            return 'NO'
        if j >= 2 * b:
            if mx > 0:
                return 'NO'
            mx = j
        tot += 1
    if mx > 0:
        if a < 2 * b:
            one = mx >= a and mx <= a + 2 * b - 2
            two = mx >= 2 * a and mx <= a + 3 * b - 2
            three = mx >= 3 * a and mx <= a + 4 * b - 2
            if not (one or two or three):
                return 'NO'
            if one and two or (two and three):
                return 'YES'
            if two:
                tot += 1
        if a >= 2 * b:
            if not (mx >= a and mx <= a + 2 * b - 2):
                return 'NO'
    if tot % 2 == 1:
        return 'YES'
    else:
        return 'NO'


q = int(input())
for i in range(q):
    (a, b) = list(map(int, input().split()))
    s = input()
    print(solve(a, b, s))

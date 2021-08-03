a, b, c, d = list(map(int, input().split()))
s1 = max(3 * a / 10, a - a / 250 * c)
s2 = max(3 * b / 10, b - b / 250 * d)
if s1 > s2:
    print('Misha')
if s1 < s2:
    print('Vasya')
if s1 == s2:
    print('Tie')

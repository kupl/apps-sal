from collections import Counter
n = int(input())
a = input()[:n]
b = input()[:n]
prelim = 0
for i in range(n // 2):
    c = Counter([a[i], a[n - 1 - i], b[i], b[n - 1 - i]])
    k = len(c)
    if k == 4:
        '\n        a x +2op\n        b y\n        '
        prelim += 2
    elif k == 3:
        '\n        a c  +1op\n        a b\n\n        a a  +2op\n        b c\n\n        a c  +1op\n        b b\n        '
        prelim += 2 if a[i] == a[n - 1 - i] else 1
    elif k == 2:
        '\n        3 3\n        3 5\n\n        3 5\n        3 3\n\n        2 5\n        2 5\n        '
        if 3 in list(c.values()):
            prelim += 1
if n % 2:
    if a[n // 2] != b[n // 2]:
        prelim += 1
print(prelim)

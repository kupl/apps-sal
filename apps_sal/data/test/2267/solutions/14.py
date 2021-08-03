from functools import cmp_to_key


def compare(x, y):
    if y + x < x + y:
        return -1
    if x + y < y + x:
        return 1
    if x + y == y + x:
        return 0


n = int(input())
s = []
for i in range(n):
    a = input()
    s.append(a)
r = sorted(s, key=cmp_to_key(compare), reverse=True)
for i in range(n):
    print(r[i], end="")

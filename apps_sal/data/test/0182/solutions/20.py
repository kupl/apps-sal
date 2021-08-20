def main():
    (a, b, c) = list(map(int, input().split()))
    (x, y, z) = list(map(int, input().split()))
    af = a - x
    bf = b - y
    cf = c - z
    q = sorted([af, bf, cf])
    if all((x < 0 for x in q)):
        return False
    if all((x >= 0 for x in q)):
        return True
    if q[0] < 0 and q[1] < 0:
        return q[2] // 2 >= -q[0] + -q[1]
    if q[0] < 0:
        return q[1] // 2 + q[2] // 2 >= -q[0]


if main():
    print('Yes')
else:
    print('No')

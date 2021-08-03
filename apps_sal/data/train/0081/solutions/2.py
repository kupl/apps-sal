t = int(input())


def test(a, b, c):
    for x, y, z in zip(a, b, c):
        if not (x == z or y == z):
            return False
    return True


for _ in range(t):
    a = input()
    b = input()
    c = input()
    if test(a, b, c):
        print("YES")
    else:
        print("NO")

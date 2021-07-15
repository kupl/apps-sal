def solve(x, y):
    if y == 0:
        return False
    if y == 1 and x > 0:
        return False
    if x < y - 1:
        return False
    if (x - (y - 1)) % 2 != 0:
        return False
    return True

x, y = [int(v) for v in input().split()]
print(["No", "Yes"][solve(x, y)])


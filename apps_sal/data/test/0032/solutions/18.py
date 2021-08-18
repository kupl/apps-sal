

def solve():
    n = int(input())
    y = 0
    for _ in range(n):
        dist, direction = input().split()
        dist = int(dist)
        if direction == "South":
            y += dist
        elif direction == "North":
            y -= dist
        else:
            if y == 0 or y == 20000:
                return "NO"
        if y < 0 or y > 20000:
            return "NO"
    if y != 0:
        return "NO"
    return "YES"


def __starting_point():
    print(solve())


__starting_point()

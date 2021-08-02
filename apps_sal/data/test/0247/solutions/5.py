def colinear(p1, p2, p3):
    return (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) == 0


def create_options(points):
    p0 = points[0]
    p1 = points[1]
    p2 = points[2]
    p3 = points[3]
    if colinear(p0, p1, p2) and colinear(p1, p2, p3):
        return [(p0, p1), []], 3
    elif colinear(p0, p1, p2):
        return [(p0, p1), [p3]], 3
    elif colinear(p0, p1, p3):
        return [(p0, p1), [p2]], 3
    elif colinear(p0, p2, p3):
        return [(p0, p2), [p1]], 3
    elif colinear(p1, p2, p3):
        return [(p1, p2), [p0]], 3
    else:
        p4 = points[4]
        if colinear(p0, p1, p4):
            return [(p0, p1), [p2, p3]], 4
        elif colinear(p0, p2, p4):
            return [(p0, p2), [p1, p3]], 4
        elif colinear(p0, p3, p4):
            return [(p0, p3), [p1, p2]], 4

        elif colinear(p1, p2, p4):
            return [(p1, p2), [p0, p3]], 4
        elif colinear(p1, p3, p4):
            return [(p1, p3), [p0, p2]], 4

        elif colinear(p2, p3, p4):
            return [(p2, p3), [p0, p1]], 4
    return False, 4


def solution(points):
    if len(points) <= 4:
        return True
    options, last = create_options(points)

    if not options:
        return False

    for p in points[last + 1:]:
        if not colinear(options[0][0], options[0][1], p):
            if len(options[1]) < 2:
                options[1].append(p)
            elif not colinear(options[1][0], options[1][1], p):
                return False
    return True


def __starting_point():
    n = int(input())
    points = [
        tuple(map(int, input().split()))
        for _ in range(n)
    ]
    print("YES" if solution(points) else "NO")


__starting_point()

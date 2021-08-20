import math
n = int(input())
xs = [int(s) for s in input().split()]
max_x = -math.inf
min_x = +math.inf
for x in xs:
    max_x = max(max_x, x)
    min_x = min(min_x, x)
if max_x <= min_x + 1:
    print(n)
    print(' '.join((str(x) for x in xs)))
else:
    max_count = sum((x == max_x for x in xs))
    min_count = sum((x == min_x for x in xs))
    middle_count = n - max_count - min_count
    solution = [max_x] * (max_count - min_count) + [min_x] * (min_count - max_count)
    equal = len(solution)
    if middle_count <= (n - len(solution)) / 2:
        equal += middle_count
        solution += [max_x - 1] * (n - len(solution))
    else:
        equal += n - len(solution) - middle_count
        solution += [max_x, min_x] * ((n - len(solution)) // 2)
        if len(solution) != n:
            solution += [max_x - 1]
            equal += 1
    print(equal)
    print(' '.join((str(x) for x in solution)))

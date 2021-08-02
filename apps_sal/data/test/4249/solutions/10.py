nb_cups, nb_task = [int(x) for x in input().split()]
caffines = sorted([int(x) for x in input().split()], reverse=True)


def check(d):
    done = 0
    for i, v in enumerate(caffines):
        done += max(0, v - i // d)
    return done >= nb_task


if sum(caffines) < nb_task:
    print(-1)
else:
    left, rite = 1, nb_cups
    mid = left + rite >> 1
    while left < rite:
        if check(mid):
            rite = mid
        else:
            left = mid + 1
        mid = left + rite >> 1
    print(left)

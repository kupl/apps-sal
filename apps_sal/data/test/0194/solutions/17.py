# IAWT
n, a, b = list(map(int, input().split()))
l = list(map(int, input().split()))
empty_one = a
empty_two = b
half_two = 0
denies = 0


def handle(group):
    nonlocal empty_one, empty_two, half_two, denies
    if group == 1:
        if empty_one > 0:
            empty_one -= 1
            return
        if empty_two > 0:
            empty_two -= 1
            half_two += 1
            return
        if half_two > 0:
            half_two -= 1
            return
        denies += 1
        return
    elif group == 2:
        if empty_two > 0:
            empty_two -= 1
            return
        denies += 2
        return


for i in range(n):
    handle(l[i])

print(denies)

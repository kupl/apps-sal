n, m = list(map(int, input().split()))

(a, d) = ([], [])

for i in range(n):

    t, val = input().split()

    (a if t == 'ATK' else d).append(int(val))

my = sorted([int(input()) for i in range(m)])

a.sort()

d.sort()


def solve1():

    ret = 0

    used = [False] * m

    for val in d:

        for i in range(m):

            if not used[i] and my[i] > val:

                used[i] = True

                break

        else:

            return 0

    for val in a:

        for i in range(m):

            if not used[i] and my[i] >= val:

                used[i] = True

                ret += my[i] - val

                break

        else:

            return 0

    return ret + sum([my[i] for i in range(m) if not used[i]])


def solve2():

    ret = 0

    for k in range(min(len(a), m)):

        if my[-k - 1] >= a[k]:
            ret += my[-k - 1] - a[k]

        else:
            break

    return ret


print(max(solve1(), solve2()))

n = int(input())
array = sorted(list(map(int, input().split())))


def all_same(items):
    return all((x == items[0] for x in items))


if n == 1:
    print(-1)
elif n == 2:
    t = max(array) - min(array)
    if t == 0:
        print(1)
        print(array[0])
    elif t % 2 == 0:
        print(3)
        print(min(array) - t, int(min(array) + t / 2), max(array) + t)
    else:
        print(2)
        print(min(array) - t, max(array) + t)
else:
    diff = [array[i + 1] - array[i] for i in range(n - 1)]
    if all_same(diff):
        t = array[1] - array[0]
        if t == 0:
            print(1)
            print(array[0])
        else:
            print(2)
            print(min(array) - t, max(array) + t)
    elif max(diff) == 2 * min(diff) and diff.count(max(diff)) == 1:
        print(1)
        print(array[diff.index(max(diff))] + min(diff))
    else:
        print(0)

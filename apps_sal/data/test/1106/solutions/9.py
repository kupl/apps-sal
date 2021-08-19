def get_lights_in_subtree(data, i):
    total = 0
    if i < len(data):
        total += data[i]
    else:
        return 0
    total += get_lights_in_subtree(data, 2 * i + 1)
    total += get_lights_in_subtree(data, 2 * i + 2)
    return total


def count_needed_lights(data, i):
    if i >= len(data):
        return (0, 0)
    l1 = count_needed_lights(data, 2 * i + 1)
    l2 = count_needed_lights(data, 2 * i + 2)
    total = l1[0] + l2[0]
    total += abs(l1[1] - l2[1])
    return (total, max(l1[1], l2[1]) + data[i])


def __starting_point():
    n = int(input())
    data = [0] + list(map(int, input().split()))
    print(count_needed_lights(data, 0)[0])


__starting_point()

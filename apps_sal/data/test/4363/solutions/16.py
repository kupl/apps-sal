(k, n) = list(map(int, input().split()))


def the_algorithm(k, n):
    count = 0
    for x in range(k + 1):
        for y in range(k + 1):
            z = n - x - y
            if 0 <= z <= k:
                count += 1
    return count


print(the_algorithm(k, n))

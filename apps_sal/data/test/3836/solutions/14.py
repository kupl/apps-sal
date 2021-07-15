def read():
    return []


def main():
    n = int(input())
    d = [[], [], [], []]

    for _ in range(n):
        key, influence = input().split()
        key = int(key, 2)
        d[key].append(int(influence))

    for key in range(4):
        d[key].sort(reverse=True)

    ans = sum(d[3])
    additional = len(d[3])

    container = []
    if len(d[1]) < len(d[2]):
        container = d[2]
    elif len(d[1]) > len(d[2]):
        container = d[1]
    container_start = min(len(d[1]), len(d[2]))
    zeros_start = 0

    for a1, a2 in zip(d[1], d[2]):
        ans += a1 + a2

    while (container_start < len(container) or zeros_start < len(d[0])) and additional:
        t1, t2 = 0, 0
        if container_start < len(container):
            t1 = container[container_start]
        if zeros_start < len(d[0]):
            t2 = d[0][zeros_start]
        if t1 < t2:
            ans += t2
            zeros_start += 1
        elif t1 >= t2 and t1 != 0:
            ans += t1
            container_start += 1
        additional -= 1

    print(ans)


def __starting_point():
    main()

__starting_point()

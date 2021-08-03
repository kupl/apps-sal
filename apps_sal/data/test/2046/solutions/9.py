def solve(snecks):
    counted_snecks = []
    for i in range(len(snecks)):
        counted_snecks.append([snecks[i], i])
    counted_snecks = sorted(counted_snecks, key=lambda x: x[0], reverse=True)

    for i in range(1, len(counted_snecks)):
        if counted_snecks[i][1] < counted_snecks[i - 1][1]:
            counted_snecks[i][1] = counted_snecks[i - 1][1]
    return counted_snecks


def __starting_point():
    n = int(input())
    snecks = list(map(int, input().split()))

    counted_snecks = solve(snecks)

    printing_array = [[] for _ in range(len(counted_snecks))]

    for cs in counted_snecks:
        printing_array[cs[1]].append(cs[0])

    for el in printing_array:
        print(" ".join(list(map(str, el))))


__starting_point()

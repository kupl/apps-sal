import statistics


def solve(array, d):
    minval = min(array)
    for i in range(len(array)):
        if (array[i] - minval) % d:
            return -1
        array[i] //= d

    median = round(statistics.median(array))
    moves = 0
    for el in array:
        moves += abs(el - median)

    return moves


line = input()
n, m, d = list(map(int, line.strip().split()))
array = []

for i in range(n):
    line = input()
    row = list(map(int, line.strip().split()))
    array += row

print(solve(array, d))

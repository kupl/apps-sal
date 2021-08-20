sq2 = 2 ** 0.5


def PyraVolume(number, edge_length):
    el3 = edge_length ** 3
    if number == 3:
        return el3 / (6 * sq2)
    elif number == 4:
        return el3 / (3 * sq2)
    elif number == 5:
        return el3 * (5 + 5 ** 0.5) / 24


(a, b, c) = list(map(int, input().split()))
print(PyraVolume(3, a) + PyraVolume(4, b) + PyraVolume(5, c))

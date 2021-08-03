from sys import stdin


def main():
    '''
    name: Kevin S. Sanchez
    '''
    inp = stdin
    wires = int(inp.readline())
    Lwires = list(map(int, inp.readline().split()))
    nums = int(inp.readline())
    electro = dict()
    for i in range(0, wires):
        electro[str(i)] = Lwires[i]

    for i in range(0, nums):
        x, y = list(map(int, inp.readline().split()))
        x = x - 1
        temp = electro[str(x)] - 1
        left = y - 1
        right = temp - left
        prox, ante = x + 1, x - 1
        electro[str(x)] = 0
        if (prox < wires and prox >= 0):
            electro[str(prox)] = electro[str(prox)] + right

        if (ante >= 0 and ante < wires):
            electro[str(ante)] = electro[str(ante)] + left

    for i in range(0, wires):
        print(str(electro[str(i)]))


main()

def main():
    array = []
    lel = input()
    lel = lel.split()
    lel[0] = int(lel[0])
    lel[1] = int(lel[1])
    quantity = 0
    for item in range(lel[0]):
        array.append(int(input()))
    for item in array:
        lel[1] -= item
        quantity += 1
    quantity += lel[1] // min(array)
    print(quantity)


def __starting_point():
    main()


__starting_point()

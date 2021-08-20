def main():
    n = int(input())
    clone = set(['R', 'G', 'B'])
    lamps = [i for i in input()]
    c = 0
    for i in range(len(lamps) - 1):
        if lamps[i] == lamps[i + 1] and i != len(lamps) - 2:
            t = clone - set([lamps[i], lamps[i + 2]])
            lamps[i + 1] = t.pop()
            c += 1
        if lamps[i] == lamps[i + 1] and i == len(lamps) - 2:
            t = clone - set([lamps[i]])
            lamps[i + 1] = t.pop()
            c += 1
    print(c)
    print(''.join(lamps))


main()

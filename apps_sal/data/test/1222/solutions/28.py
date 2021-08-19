def main():
    k = int(input())
    sm = 9
    d = {}
    lunlun = [i for i in range(1, 10)]
    for i in range(10):
        d[1, i] = ([str(i)], 1)
    dig = 2
    while sm < k:
        for i in range(10):
            out = []
            length = 0
            for j in (-1, 0, 1):
                if i + j < 0 or i + j > 9:
                    continue
                out += [str(i) + x for x in d[dig - 1, i + j][0]]
                length += d[dig - 1, i + j][1]
            d[dig, i] = (out, length)
            if i >= 1:
                sm += length
                lunlun += out
        dig += 1
    print(lunlun[k - 1])


main()

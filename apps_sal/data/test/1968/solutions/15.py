from sys import stdin


def main():
    '''
    Name KevinSS
    Code: A. Valera and Antique Items
    '''
    inp = stdin
    n, v = list(map(int, inp.readline().strip().split()))
    dicti = dict()
    sellers = list()

    for i in range(1, n + 1):
        a = str(i)
        Items = [int(x) for x in inp.readline().strip().split()]
        dicti[a] = Items

    for i in range(1, n + 1):
        flag = False
        for j in range(1, len(dicti[str(i)])):
            if (dicti[str(i)][j] < v) and flag == False:
                sellers.append(str(i))
                flag = True
    print(len(sellers))
    print(' '.join(sellers))


main()

from operator import itemgetter


def main():
    total_num = int(input())
    laptops = []
    for i in range(total_num):
        laptops.append([int(i) for i in input().split()])
    laptops = sorted(laptops, key=itemgetter(0))
    res = all(laptops[i][1] <= laptops[i + 1][1] for i in range(len(laptops) - 1))
    if res:
        print("Poor Alex")
    else:
        print("Happy Alex")


def __starting_point():
    main()
__starting_point()

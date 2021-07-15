GI = lambda: int(input()); GIS = lambda: list(map(int, input().split())); LGIS = lambda: list(GIS())

def main():
    GI()
    xs = GIS()
    ps = [[], []]
    for x in xs:
        ps[x % 2].append(x)
    ps.sort(key=len)
    lendiff = len(ps[1]) - len(ps[0])
    if lendiff > 1:
        large = ps[1]
        large.sort()
        print(sum(large[:lendiff-1]))
    else:
        print(0)

main()


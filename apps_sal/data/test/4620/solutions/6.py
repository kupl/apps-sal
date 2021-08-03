
def main():
    with open(0) as f:
        N = int(f.readline())
        train = [tuple(map(int, line.split())) for line in f.readlines()]

    ans = []
    for start in range(N - 1):
        arrive = 0
        for station in range(start, N - 1):
            c, s, f = train[station]
            # 出発時間:区間[arrive,)の下限
            def departure(arrive): return (arrive + f - 1) // f * f if arrive >= s else s
            arrive = departure(arrive) + c
        ans.append(arrive)
    ans.append(0)
    for x in ans:
        print(x)


main()

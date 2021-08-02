from copy import deepcopy


def main():
    n, k = map(int, input().split())
    a = [int(x) - 1 for x in input().split()]
    visited = set()
    i = 0
    cnt = 0
    # 途中で前に行ったところに行ったら終わり
    # kが小さくてcnt == kになってもおわり
    while True:
        if i in visited:
            break
        visited.add(i)
        cnt += 1
        i = a[i]
        if cnt == k:
            print(i + 1)
            return
    k -= cnt
    period = list()
    period.append(i)
    i = a[i]
    # 何回で同じ場所に戻るか
    while True:
        if i == period[0]:
            break
        period.append(i)
        i = a[i]
    # 余り
    mod = k % len(period)
    ans = period[mod]
    print(ans + 1)


def __starting_point():
    main()


__starting_point()

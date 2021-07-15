from collections import deque


def main():
    n, m = list(map(int, input().split()))
    test = list(map(int, input().split()))
    prepare = list(map(int, input().split()))
    least_days = sum(prepare) + m

    if least_days > len(test):
        print(-1)
        return
    index = list()
    for p in range(m + 1):
        index.append(deque())
    for t in range(len(test)):
        if test[t] == 0:
            continue
        index[test[t]].append(t)
        if t >= least_days - 1:
            index[0].append(t)
    if deque([]) in index:
        print(-1)
        return
    min_index = max(list([x.popleft() for x in index[1:]]))
    min_index = max(least_days - 1, min_index)
    for x in index[0]:
        if x >= min_index:
            print(x + 1)
            break


def __starting_point():
    main()

__starting_point()

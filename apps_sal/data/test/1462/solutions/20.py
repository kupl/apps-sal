from collections import Counter


def __starting_point():
    n, k = [int(i) for i in input().split()]
    
    c = Counter(input())

    res = 0
    tmp = k

    for w, n in c.most_common():
        if tmp > n:
            tmp -= n
            res += n * n
        else:
            res += tmp * tmp
            break
    print(res)


__starting_point()

for _ in range(int(input())):
    n = int(input())
    freq = [0] * 101
    for e in map(int, input().split()):
        freq[e] += 1
    res = 0
    one = False
    for i in range(101):
        if freq[i] == 0:
            break
        if one:
            res += 1
        else:
            if freq[i] > 1:
                res += 2
            else:
                one = True
                res += 1
    print(res)


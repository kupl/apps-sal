import itertools


def king():
    n = int(input())
    s = input()
    a = []
    for i in range(len(s)):
        if s[i] == "*":
            a.append(i + 1)

    # print(a)
    if len(a) < 5:
        print("no")
        return
    for arr in itertools.combinations(a, 5):
        arr = sorted(arr)
        mine = []
        for i in range(4):
            mine.append(arr[i + 1] - arr[i])
        if len(set(mine)) == 1:
            print("yes")
            return

    print("no")
    return


king()

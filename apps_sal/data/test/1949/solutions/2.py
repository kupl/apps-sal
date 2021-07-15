
def solve():
    n, k = [int(x) for x in input().split()]
    arr =  [int(x) for x in input().split()] + [0]
    arr.sort()
    diffs = [x - y for x, y in zip(arr[1:], arr[:-1])]
    idx = 0
    for _ in range(k):
        while idx < len(diffs) and diffs[idx] == 0:
            idx += 1

        if idx < len(diffs):
            print(diffs[idx])
            idx += 1
        else:
            print(0)


solve()



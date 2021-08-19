BIG = 10000000000


def main(n, arr):
    dist = BIG
    res = []
    for x in arr:
        if x == 0:
            dist = 0
        elif dist != BIG:
            dist += 1
        res.append(dist)
    dist = BIG
    for i in range(len(arr) - 1, -1, -1):
        x = arr[i]
        if x == 0:
            dist = 0
        elif dist != BIG:
            dist += 1
        if res[i] > dist:
            res[i] = dist
    print(' '.join(map(str, res)))


n = int(input())
arr = [int(x) for x in input().split()]
main(n, arr)

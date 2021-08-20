from operator import itemgetter


def my_sum(x):
    res = 0
    for v in x:
        res += v[1]
    return res


def main():
    n = int(input())
    left = []
    right = []
    for i in range(n):
        s = list(map(int, input().split()))
        if s[0] < 0:
            left.append(s)
        else:
            right.append(s)
    res = 0
    if len(left) < len(right):
        res += my_sum(left)
        sr = sorted(right)
        for v in range(len(left) + 1):
            res += sr[v][1]
    else:
        res += my_sum(right)
        sr = sorted(left, key=itemgetter(0), reverse=True)
        for v in range(min(len(right) + 1, len(left))):
            res += sr[v][1]
    print(res)


main()

n = int(input())
a = [int(i) for i in input().split()]
a1 = [[-1] * 50, [-1] * 50]


def get(i, fl):
    if i >= n:
        return 0
    if (a1[fl][i] != -1):
        return a1[fl][i]
    if fl == 0:
        a1[fl][i] = max(a[i] + get(i + 1, 1), get(i + 1, 0))
    else:
        a1[fl][i] = min(a[i] + get(i + 1, 1), get(i + 1, 0))
    return a1[fl][i]


an = get(0, 0)
print(sum(a) - an, an)

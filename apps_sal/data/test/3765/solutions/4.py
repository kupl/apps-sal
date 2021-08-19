a, b, h, w, n = list(map(int, input().strip().split(' ')))
if a > b:
    a, b = b, a

factor = list(map(int, input().strip().split(' ')))
factor = sorted(factor)[::-1]
# print(factor)


def findout(a, b, h, w, factor):
    possible = set()
    for i in range(len(factor)):
        temp = set()
        if i == 0:
            temp.add((factor[0], 1))
            temp.add((1, factor[0]))
            possible = temp
            for X in temp:
                f1, f2 = X
                if f1 * h >= a and f2 * w >= b:
                    return i + 1

        else:
            for X in possible:
                c1, c2 = X
                if c1 * h <= a:
                    temp.add((c1 * factor[i], c2))
                    if c1 * factor[i] * h >= a and c2 * w >= b:
                        return i + 1

                if c2 * w <= b:
                    temp.add((c1, c2 * factor[i]))
                    if c1 * h >= a and c2 * w * factor[i] >= b:
                        return i + 1
            possible = temp
    return 10**9 + 1


if (h >= a and w >= b) or (h >= b and w >= a):
    print(0)
else:
    ans = min(findout(a, b, h, w, factor), findout(a, b, w, h, factor))
    if ans != 10**9 + 1:
        print(ans)
    else:
        print(-1)

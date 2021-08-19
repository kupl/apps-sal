N = int(input())
A = list(map(int, input().split()))


def count(X, Y):
    res = 0
    r = 0
    r2 = 0
    Y = [-10 ** 10] + Y + [10 ** 10]
    for l in range(len(X)):
        xl = X[l]
        for _ in range(len(Y)):
            if Y[r + 1] <= 2 * xl:
                r += 1
                continue
            break
        for _ in range(len(Y)):
            if Y[r2 + 1] < xl:
                r2 += 1
                continue
            break
        res += max(0, r - r2)
    return res


AP = [a for a in A if a > 0]
AP.sort()
AN = [-a for a in A if a < 0]
AN.sort()
print(count(AP, AP) + count(AP, AN) + count(AN, AP) + count(AN, AN) - len(AN) - len(AP) - len(set(AP) & set(AN)))

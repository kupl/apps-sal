def xor_next(values):
    result = [0] * len(values)
    for i in range(len(values)):
        result[i] = values[i] ^ values[(i + 1) % len(values)]
    return result


def make_mp_table(values):
    result = [-1] * (len(values) + 1)
    j = -1
    for i in range(len(values)):
        while j != -1 and values[j] != values[i]:
            j = result[j]
        j += 1
        result[i + 1] = j
    return result


def mp_find(target, pattern, table):
    result = []
    j = 0
    for i in range(len(target)):
        while j != -1 and pattern[j] != target[i]:
            j = table[j]
        j += 1
        if j == len(pattern):
            result.append(i - (j - 1))
            j = table[j]
    return result


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    xa = xor_next(a)
    xb = xor_next(b)
    mp_t = make_mp_table(xa)
    xb += xb
    res = mp_find(xb, xa, mp_t)
    res.sort(reverse=True)
    for i in range(len(res)):
        k = n - res[i]
        if k >= n:
            continue
        x = a[k] ^ b[0]
        print(str(k) + ' ' + str(x))


main()

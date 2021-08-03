K = int(input())


def list2int(digits):
    return int("".join(map(str, digits)))


def int2list(n):
    return list(map(int, str(n)))


def search(digits):
    ret = []
    v = digits[-1]
    for d in [-1, 0, 1]:
        if 0 <= v + d <= 9:
            ret.append(list2int(digits + [v + d]))
    return(ret)


result = list(range(1, 9 + 1))

i = 0
while len(result) < K:
    digits = int2list(result[i])
    result.extend(search(digits))
    i += 1

print((result[K - 1]))

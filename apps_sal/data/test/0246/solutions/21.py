def read_ints():
    return list(map(int, input().split()))


(n, s) = read_ints()


def judge(x):
    return x - sum(map(int, str(x))) >= s


result = len([x for x in range(s, min(n, s + 180) + 1) if judge(x)]) + max(0, n - s - 180)
print(result)

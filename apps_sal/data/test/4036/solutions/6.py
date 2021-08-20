_ = input().split()
n = int(_[0])
k = int(_[1])


def lower(k, i):
    return k * i + int(k * (k - 1) / 2)


def _max(k, i):
    return i * (pow(2, k) - 1)


if n < lower(k, 1):
    print('NO')
else:
    i = int((n - int(k * (k - 1) / 2)) / k) - 1
    while lower(k, i) <= n:
        i = i + 1
    i = i - 1
    if _max(k, i) < n:
        print('NO')
    else:
        answer = [_ + i for _ in range(k)]
        adder = n - lower(k, i)
        for _ in range(adder):
            answer[-_ - 1] = answer[-_ - 1] + 1
        if k > 2 and answer[0] == 1 and (answer[1] == 3):
            answer[1] = answer[1] - 1
            answer[-1] = answer[-1] + 1
        answer = [str(_) for _ in answer]
        print('YES')
        print(' '.join(answer))

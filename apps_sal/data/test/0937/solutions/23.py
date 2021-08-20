def calculate_prefix_sum(a, t):
    s = [0]
    for (a_, t_) in zip(a, t):
        if not t_:
            s += [s[-1] + a_]
        else:
            s += [s[-1]]
    return s


def calculate_sum_on_range(s, a, b):
    assert a < b
    return s[min(b, len(s) - 1)] - s[a]


def calculate_sums(a, t, k):
    psum = calculate_prefix_sum(a, t)
    s = []
    for i in range(len(a)):
        s.append(calculate_sum_on_range(psum, i, i + k))
    return s


def calculate_max(a, t, k):
    s = calculate_sums(a, t, k)
    ms = max(s)
    return ms


def calculate_answer(a, t, k):
    ms = calculate_max(a, t, k)
    s = 0
    for (a_, t_) in zip(a, t):
        if t_:
            s += a_
    return ms + s


def r():
    return list(map(int, input().split()))


(_, k) = r()
print(calculate_answer(r(), r(), k))

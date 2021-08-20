(n, a, b) = list(map(int, input().split()))


def solve(n, a, b):
    rev = a < b
    if rev:
        (b, a) = (a, b)
    if n < a + b - 1:
        return [-1]
    if n > a * b:
        return [-1]
    surrogate_ans = []
    for i in range(b):
        nd = i + 1
        reminder = n - a * i
        tail = b - nd
        batch_length = min(a, reminder - tail)
        batch = list(range(n + 1 - a * i - batch_length, n + 1 - a * i))
        surrogate_ans += batch
        if batch_length != a:
            surrogate_ans += list(reversed(list(range(1, tail + 1))))
        if len(surrogate_ans) == n:
            break
    if rev:
        return reversed(surrogate_ans)
    else:
        return surrogate_ans


print(' '.join(map(str, solve(n, a, b))))

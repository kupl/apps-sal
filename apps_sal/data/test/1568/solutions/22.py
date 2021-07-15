def solution(n, a, b, c, t, messages):
    account = 0
    for m in messages:
        if b >= c:
            account += a
        else:
            account += (c - b) * (t - m) + a
    return account

n, a, b, c, t = list(map(int, input().split()))
messages = list(map(int, input().split()))
print(solution(n, a, b, c, t, messages))


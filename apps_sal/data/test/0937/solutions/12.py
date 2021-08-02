def read_data():
    n, m = map(int, list(input().strip().split()))
    a = list(map(int, list(input().strip().split())))
    b = list(map(int, list(input().strip().split())))
    return n, m, a, b


def solve():
    val = 0
    for i in range(n):
        if b[i] == 1:
            val += a[i]
    for i in range(k):
        if b[i] == 0:
            val += a[i]
    i = k
    max = val
    while i < n:
        if b[i - k] == 0:
            val -= a[i - k]
        if b[i] == 0:
            val += a[i]
        if val > max:
            max = val
        i += 1
    return max


n, k, a, b = read_data()
print(solve())

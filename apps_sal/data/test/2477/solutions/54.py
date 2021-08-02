N, K = list(map(int, input().split()))
*A, = list(map(int, input().split()))


def f(t):
    return sum(i // t if i != t else 0 for i in A) <= K if t else all(i <= t for i in A)


l, r = -1, 10**10
while r - l > 1:
    m = (r + l) // 2
    if f(m):
        r = m
    else:
        l = m

print(r)

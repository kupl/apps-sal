def f(x, l, r):
    result = x[l]
    for i in x[l + 1:r + 1]:
        result |= i
    return result


def foo(a, b, n):
    max_a = max(a)
    max_b = max(b)
    a, max_a, b, max_b = (a, max_a, b, max_b) if max_a > max_b else (b, max_b, a, max_a)
    l = r = a.index(max_a)
    while r < n and f(a, l, r) + f(b, l, r) <= f(a, l, r + 1) + f(b, l, r + 1):
        r += 1
    while l > 0 and f(a, l, r) + f(b, l, r) <= f(a, l - 1, r) + f(b, l - 1, r):
        l -= 1
    return f(a, l, r) + f(b, l, r)


n = int(input())
a = [int(n) for n in input().split()]
b = [int(n) for n in input().split()]
max_a = max(a)
max_b = max(b)
a, max_a, b, max_b = (a, max_a, b, max_b) if max_a > max_b else (b, max_b, a, max_a)
l = r = a.index(max_a)
while r < n and f(a, l, r) + f(b, l, r) <= f(a, l, r + 1) + f(b, l, r + 1):
    r += 1
while l > 0 and f(a, l, r) + f(b, l, r) <= f(a, l - 1, r) + f(b, l - 1, r):
    l -= 1
print(f(a, l, r) + f(b, l, r))

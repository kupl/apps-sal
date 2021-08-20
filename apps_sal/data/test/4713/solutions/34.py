(N, S) = (input(), input())
(x, xmax) = (0, 0)
for s in S:
    x = (lambda a: x + 1 if a == 'I' else x - 1)(s)
    xmax = max(x, xmax)
print(xmax)

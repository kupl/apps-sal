def f():
    return [*map(int, input().split())]


(n, h) = f()
(A, B) = ([], [])
for _ in range(n):
    (a, b) = f()
    A += [a]
    B += [b]
m = max(A)
B.sort()
c = 0
for b in sorted(B)[::-1]:
    if b > m:
        h -= b
        c += 1
        if h < 1:
            break
print(c - -h // m * (h > 0))

def f(): return [*map(int, input().split())]


n, h = f()
A, B = [], []
for _ in range(n):
    a, b = f()
    A += [a]
    B += [b]
m = max(A)
B.sort()
c = 0
while h > 0 and B and B[-1] > m:
    h -= B.pop()
    c += 1
print(c - -h // m * (h > 0))

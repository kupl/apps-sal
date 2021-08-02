I = lambda: map(int, input().split())
a = [0, 0]
b = [0, 0]
for _ in '0' * next(I()): c, d = I(); a[c] += 1; b[d] += 1
print(min(a) + min(b))

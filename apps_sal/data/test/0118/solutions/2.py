read = lambda: list(map(int, input().split()))
t, s, x = read()
f1 = (x - t) % s == 0 and x >= t
f2 = (x - t - 1) % s == 0 and x > t + 1
print('YES' if (f1 or f2) else 'NO')


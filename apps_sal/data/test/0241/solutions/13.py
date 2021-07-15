n, m, a, b = map(int, input().split())
t = list(map(int, input().split()))
x, y = min(t), max(t)
print('Correct' if a <= x and y <= b and len(t) + int(a < x) + int(y < b) <= n else 'Incorrect')

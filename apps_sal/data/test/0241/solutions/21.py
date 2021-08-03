def I(): return list(map(int, input().split()))


n, m, N, X = I()
t = I()
r = min(t) != N
r += max(t) != X
print(['C', 'Inc'][m + r > n or min(t) < N or max(t) > X] + 'orrect')

N, M, X = map(int, input().split())
A = [*map(int, input().split())]
l = [i < X for i in A]
r = [i > X for i in A]
print(l.count(False) if l.count(False) < r.count(False) else r.count(False))

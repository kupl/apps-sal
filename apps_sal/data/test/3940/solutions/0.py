def f(): return list(map(int, input().split()))


n, m = f()
def lr(x): return x[1] - x[0] + 1


sq = min(lr(f()) for _ in range(m))
print(sq)
x = ' '.join([str(i % sq) for i in range(n)])
print(x)

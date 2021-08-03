def f(): return map(int, input().split())


N, K = f()
for a, b in sorted([*f()]for _ in [0] * N):
    K -= b
    if K < 1:
        print(a)
        return

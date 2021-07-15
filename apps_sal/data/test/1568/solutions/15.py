R = lambda: list(map(int, input().split()))

n, A, B, C, T = R()
s = 0
for t in R():
    a = (T-t)*(C-B) if B<C else 0
    s += A + a
print(s)



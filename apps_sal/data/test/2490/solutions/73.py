N = list(map(int, input()))

m = 0
m_ = 1

for n in N:
    m, m_ = min(m + n, m_ + 10 - n), min(m + n + 1, m_ + 10 - (n + 1))
print(m)

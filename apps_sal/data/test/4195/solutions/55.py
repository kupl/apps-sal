D, N = map(int, input().split())
l = []

for i in range(1, 1100000):
    if i % 100**D == 0 and i % 100**(D + 1) != 0:
        l.append(i)
print(l[N - 1])

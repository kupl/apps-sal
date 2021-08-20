N = int(input())
ls = [0] * (N + 1)
(ls[0], ls[1]) = (2, 1)
for i in range(2, N + 1):
    ls[i] += ls[i - 1] + ls[i - 2]
print(ls[N])

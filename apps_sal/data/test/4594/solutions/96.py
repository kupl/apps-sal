N = int(input())
d = list([0] * N)
for i in range(N):
    d[i] = int(input())
d = set(d)
print(len(d))

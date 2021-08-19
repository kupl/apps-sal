(n, m) = list(map(int, input().split()))
s = set((i for i in range(1, m + 1)))
for i in range(n):
    (k, *a) = list(map(int, input().split()))
    s &= set(a)
print(len(s))

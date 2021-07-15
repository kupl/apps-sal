n, m = map(int, input().split())

a = set(range(1, m + 1))
for _ in range(n):
    k, *aa = map(int, input().split())
    a = a & set(aa)

print(len(a))

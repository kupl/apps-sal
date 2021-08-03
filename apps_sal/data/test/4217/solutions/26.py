n, m = map(int, input().split())
s = set(range(1, 1 + m))
for _ in range(n):
    k, *a = map(int, input().split())
    s &= set(a)
print(len(s))

import collections as c
print(sum((i * (i - 1) // 2 for i in c.Counter((''.join(sorted(input())) for _ in range(int(input())))).values())))

n = int(input())
a = [int(i) for i in input().split()]
mn = -100000000000000
for i in a:
    if i < 0:
        mn = max(mn, i)
        continue
    v = int(i ** 0.5)
    if v * v != i and (v + 1) * (v + 1) != i and (v - 1) * (v - 1) != i:
        mn = max(mn, i)
print(mn)


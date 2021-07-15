N, x = map(int, input().split())
values = map(int, input().split())
count = 0
v1 = next(values)
for v2 in values:
    surplus = max(v1 + v2 - x, 0)
    count += surplus
    v1 = max(0, v2 - surplus)
print(count)

s = map(int, input().split())
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
both_have_num = 10
for i1 in a:
    for i2 in b:
        if i1 == i2:
            both_have_num = min(both_have_num, i1)
min_a = min(a)
min_b = min(b)
ans = 0
if both_have_num < 10:
    print(both_have_num)
else:
    print(min(min_a, min_b) * 10 + max(min_a, min_b))

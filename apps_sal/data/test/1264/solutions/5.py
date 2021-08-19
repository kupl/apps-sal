n = int(input())
a = list(map(int, input().split()))
one_count = 0
(lcs, cur) = (0, 0)
for i in a:
    if i == 1:
        one_count += 1
        cur = max(0, cur - 1)
    else:
        cur += 1
        lcs = max(lcs, cur)
print(one_count + lcs if one_count != n else one_count - 1)

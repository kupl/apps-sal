n = int(input())
nums = list(map(int, input().split()))

pos = [x for x in nums if x > 0]
neg = [x for x in nums if x < 0]

s1 = sum(pos)
if s1 % 2 == 1:
    print(s1)
    return

podd = [x for x in pos if x % 2 == 1]
nodd = [x for x in neg if x % 2 == 1]


if podd:
    min_podd = min(podd)
    if not nodd:
        s1 -= min_podd
    else:
        max_nodd = max(nodd)
        if min_podd + max_nodd > 0:
            s1 += max_nodd
        else:
            s1 -= min_podd
else:
    s1 += max(nodd)


print(s1)


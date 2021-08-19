import math
[n] = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
sqr_list_dist = []
non_sqr_dist = []
for i in a:
    if i ** 0.5 % 1 == 0:
        if i == 0:
            sqr_list_dist.append(2)
        else:
            sqr_list_dist.append(1)
    else:
        lower = math.floor(i ** 0.5) ** 2
        upper = math.ceil(i ** 0.5) ** 2
        non_sqr_dist.append(min(i - lower, upper - i))
diff = len(sqr_list_dist) - n // 2
if diff == 0:
    print(0)
elif diff > 0:
    sqr_list_dist.sort()
    print(sum(sqr_list_dist[:diff]))
else:
    non_sqr_dist.sort()
    print(sum(non_sqr_dist[:abs(diff)]))

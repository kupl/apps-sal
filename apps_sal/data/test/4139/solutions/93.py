import itertools
import bisect

num_list = []
for i in range(3, 10):
    num_list += list(itertools.product('753', repeat=i))

num = []
for nm in num_list:
    if '3' in nm and '5' in nm and '7' in nm:
        num.append(int(''.join(nm)))

num.sort()
print((bisect.bisect_right(num, int(input()))))

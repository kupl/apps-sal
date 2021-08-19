n = int(input())
a = sorted(list(map(int, input().split())))
duplicates = {}
d = None
delta = 0
for (i, el) in enumerate(a, 1):
    if el not in duplicates:
        duplicates[el] = 0
    else:
        d = el
        duplicates[el] += 1
    min_value = i - 1
    delta += el - min_value
if sum(duplicates.values()) > 1 or duplicates.get(0, 0) >= 1 or (d is not None and d - 1 in duplicates):
    print('cslnb')
elif delta == 0:
    print('cslnb')
elif delta % 2 == 1:
    print('sjfnb')
else:
    print('cslnb')

from itertools import cycle
n = int(input())
l = list(map(int, input().split(' ')))

times_to_rotate = n - l[0]

for count, (i, mul) in enumerate(zip(l, cycle([1, -1]))):
    j = (i + times_to_rotate * mul) % n
    if j != count:
        print('No')
        break
else:
    print('Yes')

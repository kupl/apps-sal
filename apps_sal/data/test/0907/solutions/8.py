from collections import Counter
from itertools import chain
ab = tuple((tuple(map(int, input().split())) for _ in range(int(input().split()[[2, 1][1]]))))
for x_ in Counter(chain(*ab)).most_common(4):
    x = x_[0]
    ab2 = (abi for abi in ab if x not in abi)
    try:
        try:
            ys = set(next(ab2))
        except StopIteration:
            pass
        else:
            for abi2 in ab2:
                ys.intersection_update(abi2)
            assert ys
        print('YES')
        break
    except AssertionError:
        pass
else:
    print('NO')

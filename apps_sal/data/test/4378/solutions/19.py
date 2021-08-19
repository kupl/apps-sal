# url: https://codeforces.com/contest/1108/problem/D


def compatible(prev, *args):
    if not args:
        return next(iter(colour_set - {prev}))
    else:
        return next(iter(colour_set - {prev, args[0]}))


n_lamps = int(input())
garland = list(input())

colour_set = {'R', 'G', 'B'}
count = 0

for idx, lamp in enumerate(garland):

    if idx == 0:
        continue

    prev = garland[idx - 1]
    if lamp == prev:
        if idx == len(garland) - 1:
            garland[-1] = compatible(prev)
            count += 1
            continue

        nxt = garland[idx + 1]
        garland[idx] = compatible(prev, nxt)
        count += 1

print(count)
print(''.join(garland))

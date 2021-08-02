import itertools
import collections

x = input()

erg = -1
pos = "R B Y G".split()
for p in itertools.permutations(pos):

    t = p * 30
    t[:len(x)]

    tmp = collections.defaultdict(int)

    for i in range(len(x)):
        if x[i] == '!':
            tmp[t[i]] += 1
            continue

        if x[i] == t[i]:
            continue
        else:
            tmp = -1
            break

    if tmp == -1:
        continue
    else:
        print("{} {} {} {}".format(tmp['R'], tmp['B'], tmp['Y'], tmp['G']))
        break

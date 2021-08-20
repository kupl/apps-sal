import itertools


def beauty(string, n):
    string = sorted(string)
    maxlen = 0
    for (k, g) in itertools.groupby(string):
        maxlen = max(maxlen, len(list(g)))
    if maxlen == len(string) and n == 1:
        return maxlen - 1
    else:
        return min(len(string), n + maxlen)


n = int(input())
li = []
li.append((beauty(input(), n), 'Kuro'))
li.append((beauty(input(), n), 'Shiro'))
li.append((beauty(input(), n), 'Katie'))
li.sort(reverse=True)
if li[0][0] == li[1][0]:
    print('Draw')
else:
    print(li[0][1])

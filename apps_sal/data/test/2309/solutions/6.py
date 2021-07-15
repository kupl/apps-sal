from collections import Counter
import sys


def count(word):
    lst = ''
    k = 0
    for el in word:
        if el in gl:
            k += 1
            lst = el
    return k, lst


n = int(input())
gl = set('aeoui')
d = dict()
b = dict()
for i in range(n):
    t = input()
    s = count(t)
    if s[0] in b:
        b[s[0]][t] += 1
    else:
        b[s[0]] = Counter()
        b[s[0]][t] += 1
    if s in d:
        d[s].append(t)
    else:
        d[s] = [t]
leftpair = []
rightpair = []
for el in d:
    for i in range(0, len(d[el]) - 1, 2):
        rightpair.append((d[el][i], d[el][i + 1]))
        b[el[0]][d[el][i]] -= 1
        b[el[0]][d[el][i + 1]] -= 1
# print(b)
for el in b:
    last1len = -1
    for ell in b[el]:
        if b[el][ell] % 2 == 1:
            if last1len != -1:
                leftpair[last1len].append(ell)
                last1len = -1
            else:
                leftpair.append([ell])
                last1len = len(leftpair) - 1
        for k in range(b[el][ell] // 2):
            leftpair.append((ell, ell))
    if last1len != -1:
        leftpair.pop(last1len)
if len(rightpair) > len(leftpair):
    t = (len(rightpair) + len(leftpair)) // 2
    leftpair.extend(rightpair[t:])
    rightpair = rightpair[:t]
print(min(len(leftpair), len(rightpair)))
# print(leftpair)
# print(rightpair)
for i in range(min(len(leftpair), len(rightpair))):
    sys.stdout.write(leftpair[i][0] + ' ' + rightpair[i][0] + '\n' + leftpair[i][1] + ' ' + rightpair[i][1] + '\n')


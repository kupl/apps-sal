import collections
N = int(input())
Slist = []
for i in range(N):
    Slist.append(input())
anslist = sorted(Slist)
c = collections.Counter(anslist)
(values, counts) = zip(*c.most_common())
maxcount = counts[0]
i = 0
for i in range(len(values)):
    if maxcount == counts[i]:
        print(values[i])
        maxcount = counts[i]
        i += 1
    else:
        break

import sys
from collections import Counter
from operator import itemgetter

n = int(sys.stdin.readline().strip())
if n < 3:
    print('1')
    return

times = list(enumerate(map(int, (sys.stdin.readline().split()))))
times.sort(key=itemgetter(1))

origindices = [t[0] for t in times]
times = [t[1] for t in times]


# check if we can remove the first
c = times[2] - times[1]
a = times[1]
success = True
for i in range(2,n):
    if times[i] != a + c * (i - 1):
        success = False
        break

if success:
    print(origindices[0] + 1)
    return


# check if we can remove the second
a = times[0]
c = times[2] - times[0]
success = True
for i in range(2, n):
    if times[i] != a + c * (i - 1):
        success = False
        break

if success:
    print(origindices[1] + 1)
    return


# check if we can remove any other
removednum = 1 # if everything is correct (and we don't have to delete any element), we can just delete the first one
success = True
a = times[0]
c = times[1] - times[0]
for i in range(2,n):
    if (removednum == 1 and times[i] != a + c * i) \
       or (removednum != 1 and times[i] != a + c * (i - 1)):
        # print(f'Found that {times[i]} is not equal to {a + c * i} {a}, {i}, {c}')
        if removednum == 1:
            removednum = i # maybe it will still work if we remove this one; add 1 to shift index
        else:
            # otherwise, we already have removed an element,
            # so we must conclude that there is no way to make this succeed
            success = False
            break

if success:
    print(origindices[removednum] + 1)
    return


# This should only happen when everything fails:
print(-1)




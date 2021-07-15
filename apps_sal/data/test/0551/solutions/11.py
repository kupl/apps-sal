from math import isclose

n = int(input())
y = [0] + list(map(int, input().split()))
ans = True
if n == 4:
    if (y[1] - y[3])/2 == (y[2] - y[4])/2 or \
       (y[1] - y[4])/3 == (y[2] - y[3]):
        print('Yes')
        return
catch = None
for z in [1, 2]:
    c = {}
    for i in range(z+1, len(y)):
        k = (y[i] - y[z])/(i - z)
        if k not in c:
            c[k] = 1
        else:
            catch = k
            break
    if catch != None:
        break
else:
    catch = (y[2] - y[1])

y_new = []

for i in range(2, len(y)):
    k = (y[i] - y[1])/(i - 1)
    if not isclose(k, catch):
        y_new.append((i, y[i]))
if not y_new:
    ans = False
elif len(y_new) == 1:
    ans = True
else:
    for i in range(1, len(y_new)):
        k = (y_new[0][1] - y_new[i][1])/(y_new[0][0] - y_new[i][0])
        if not isclose(catch, k):
            ans = False
            break

if ans:
    print('Yes')
else:
    print('No')
"""
6
2 -1 2 5 14 17
"""


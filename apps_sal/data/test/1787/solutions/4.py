import sys


s = input()

t = ''

for i in s:
    if(i == 'a' or i == 'b'):
        t += i


posj = []
for i in range(len(t)):
    if(t[i] == 'b'):
        posj.append(i)
if(len(posj) == 0):
    print(len(t))
    return


mids = [posj[0] + 1]

mod = 10**9 + 7
sub1 = 0
for i in range(len(posj) - 1):
    mid = posj[i + 1] - posj[i]

    mids.append(mid)
mids.append(len(t) - posj[-1])

tot = 1

for i in mids:
    tot *= i
    tot %= mod
tot -= 1
print(tot % mod)

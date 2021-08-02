__author__ = 'neki'

import sys

#sys.stdin = open("friendsPresents.in", "r")
#sys.stdout = open("friendsPresents.out", "w")

words = input().split()
cnt1 = int(words[0])
cnt2 = int(words[1])
x = int(words[2])
y = int(words[3])
#print(cnt1, cnt2, x, y)


def determine(num, x, y, cnt1, cnt2):
    like1 = num - num // x
    like2 = num - num // y
    like1and2 = like1 + like2 - num + num // (x * y)
    #print(like1, like2, like1and2)

    friend1 = like1 - like1and2
    friend2 = like2 - like1and2
    both = like1and2
    #print(num, friend1, friend2, both)

    cond1 = 0
    cond2 = 0
    if friend1 + both >= cnt1 and friend2 + both >= cnt2:
        cond1 += 1
    if friend1 + friend2 + both >= cnt1 + cnt2:
        cond2 += 1
    if cond1 > 0 and cond2 > 0:
        return 1
    return 0


lim = 0
lim1 = 1
lim2 = -1
while 1:
    if lim2 < 0:
        lim = lim1 * 2
    else:
        lim = (lim1 + lim2) // 2
    if lim == lim1:
        break
    if determine(lim, x, y, cnt1, cnt2) == 1:
        lim2 = lim
    else:
        lim1 = lim
    #print("(", lim1, lim2, ")")
print(lim2)

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 23:02:08 2019

@author: Mridul Garg
"""

n = int(input())

a = [0] * n
b = [0] * n

a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

for i in range(n):
    a[i] = [a[i], b[i]]
a.sort(reverse=True, key=lambda x: x[0])

same = []
comp = a[0][0]
count = 1
score = a[0][1]
for i in range(1, n):
    if comp == a[i][0] and i == n - 1:
        count += 1
        score += a[i][1]
        same.append([comp, score, i])

    elif comp == a[i][0]:
        count += 1
        score += a[i][1]

    else:
        if count > 1:
            same.append([comp, score, i - 1])
            comp = a[i][0]
            score = a[i][1]
            count = 1
        else:
            comp = a[i][0]
            score = a[i][1]
            count = 1

#scores = []
relevant = []

if len(same) == 0:
    print(0)

else:
    f = same[0][0]
    fscore = same[0][1]
    findex = same[0][2]

    for i in range(1, len(same)):
        if f & same[i][0] != same[i][0]:
            relevant.append(same[i][0])
#            fscore += same[i][1]

    for i in range(findex + 1, n):
        if f & a[i][0] == a[i][0]:
            fscore += a[i][1]
        else:
            for j in relevant:
                if a[i][0] & j == a[i][0]:
                    fscore += a[i][1]
                    break

    print(fscore)


# else:
#
#    for i in same:
#        score = i[1]
#        index = i[2]
#        num = i[0]
#
#        for j in range(index + 1, n):
#            if num & a[j][0] == a[j][0]:
#                score += a[j][1]
#
#        scores.append([num, score])
#
#    print(scores)
#    temp = scores[0]
#    for i in range(len(scores)):
#        print('============================================')
#        for j in range(len(scores)):
#            if scores[i][0] & scores[j][0] != scores[j][0]:
#                scores[i][1] += scores[j][1]
#                print(scores[i][1])
#
#
#    print(scores)
#    print(max(scores))

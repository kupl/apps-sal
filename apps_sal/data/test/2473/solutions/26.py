# solution

import io
import math
import scipy.sparse
import numpy

nim, mike = map(int, input().split())
array = [list(map(int, input().split())) for i in range(nim)]

answer = 10**100
sortx = sorted(array, key = lambda x: x[0])
for a, pt1 in enumerate(sortx[:nim-mike+1]):
    for b, pt2 in enumerate(sortx[a+mike-1:]):
        #print(a,b)
        sorty = sorted(sortx[a:a+mike+b], key = lambda x: x[1])
        sorty_len = len(sorty)
        for c, pt3 in enumerate(sorty[:sorty_len-mike+1]):
            #print(len(sorty), c, k)
            pt4 = sorty[c+mike-1]
            #print(pt1, pt2, pt3, pt4)
            if pt3[1] <= pt1[1] and pt3[1] <= pt2[1] and pt4[1] >= pt1[1] and pt4[1] >= pt2[1]:
                answer = min(answer, (pt2[0] - pt1[0]) * (pt4[1] - pt3[1]))
print(answer)

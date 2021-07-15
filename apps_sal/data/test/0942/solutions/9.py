from collections import Counter as C
n = int(input())
l = [*map(lambda x: n - int(x), input().split())]
c = C(l)
d = {}
# print(c)
try:
    for k, v in c.items():
        if v % k == 0:
            d[k] = v//k
        else:
            raise ValueError()
    print('Possible')
    d_ = {}
    curr = 0
    for e in l:
        # print(d, d_)
        if e in d_:
            if d_[e][1] >= e:
                curr += 1
                d_[e] = [curr, 1]
            else:
                d_[e][1] += 1
        else:
            curr += 1
            d_[e] = [curr, 1]
        print(d_[e][0], end=' ')
except:
    print('Impossible')

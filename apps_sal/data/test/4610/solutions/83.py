# cook your dish here
import operator
N, K = map(int, input().split())
lst = list(map(int, input().split()))
x = []
x = set(lst)
if len(x) <= K:
    print(0)
else:
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    # l=[]
    # l=list(freq.items())
    s = {}
    s = dict(sorted(freq.items(), key=operator.itemgetter(1)))
    # print(s)
    # l.sort()
    cc = abs(len(x) - K)
    # print(cc)
    v = 0
    for key, value in s.items():

        v += s[key]
        # print(key)
        cc -= 1
        if cc == 0:
            print(v)
            break

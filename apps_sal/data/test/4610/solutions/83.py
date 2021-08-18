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
    s = {}
    s = dict(sorted(freq.items(), key=operator.itemgetter(1)))
    cc = abs(len(x) - K)
    v = 0
    for key, value in s.items():

        v += s[key]
        cc -= 1
        if cc == 0:
            print(v)
            break

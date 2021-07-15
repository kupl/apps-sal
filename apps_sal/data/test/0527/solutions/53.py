S = list(str(input()))
T = list(str(input()))

S_ = set(list(S))
T_ = set(list(T))
for c in T:
    if c not in S_:
        print((-1))
        return

d = [[] for _ in range(26)]
for i, s in enumerate(S):
    d[ord(s)-ord('a')].append(i)
#print(d)

q = 0
pre = -1
import bisect
for t in T:
    j = ord(t)-ord('a')
    idx = bisect.bisect_right(d[j], pre)
    if idx == len(d[j]):
        q += 1
        pre = d[j][0]
    else:
        pre = d[j][idx]
print((q*len(S)+pre+1))


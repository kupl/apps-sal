import collections

n = int(input())
a = list(map(int, input().split()))
q = int(input())
s = sum(a)

ad = collections.Counter(a)

for i in range(q):
    b, c = map(int, input().split())
    s += ad.get(b, 0) * (c - b) 
    print(s)
    ad[c] += ad.get(b, 0)
    ad[b] = 0

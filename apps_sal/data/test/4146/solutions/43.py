import collections
N = int(input())
N_List = list(map(int, input().split()))
hanN = N // 2
ki = N_List[1::2]
gu = N_List[0::2]
kicnt = collections.Counter(ki)
gucnt = collections.Counter(gu)
kidict = kicnt.most_common()
gudict = gucnt.most_common()
kilen = len(kidict)
gulen = len(gudict)
if kilen == 1 & gulen == 1:
    if kidict == gudict:
        ans = hanN
    else:
        ans = 0
elif kidict[0][0] == gudict[0][0]:
    if kidict[0][1] > gudict[0][1]:
        ans = sum(map(lambda x: x[1], kidict[1:])) + sum(map(lambda x: x[1], gudict[2:])) + gudict[0][1]
    elif kidict[0][1] < gudict[0][1]:
        ans = sum(map(lambda x: x[1], gudict[1:])) + sum(map(lambda x: x[1], kidict[2:])) + kidict[0][1]
    elif gudict[1][1] >= kidict[1][1]:
        ans = sum(map(lambda x: x[1], kidict[1:])) + sum(map(lambda x: x[1], gudict[2:])) + gudict[0][1]
    else:
        ans = sum(map(lambda x: x[1], gudict[1:])) + sum(map(lambda x: x[1], kidict[2:])) + kidict[0][1]
else:
    ans = sum(map(lambda x: x[1], gudict[1:])) + sum(map(lambda x: x[1], kidict[1:]))
print(ans)

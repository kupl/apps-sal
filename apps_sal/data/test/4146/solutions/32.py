import collections
N = int(input())
V = list(map(int, input().split()))

ans = 0
eve = V[0::2]
odd = V[1::2]
cntEve = collections.Counter(eve)
cntOdd = collections.Counter(odd)

if cntEve.most_common()[0][0] == cntOdd.most_common()[0][0]:
    if len(cntEve) == 1 and len(cntOdd) > 1:
        ans = N - max(cntEve.most_common()[0][1], cntOdd.most_common()[0][1]) - cntOdd.most_common()[1][1]
    elif len(cntEve) > 1 and len(cntOdd) == 1:
        ans = N - max(cntEve.most_common()[0][1], cntOdd.most_common()[0][1]) - cntEve.most_common()[1][1]
    elif len(cntEve) == 1 and len(cntOdd) == 1:
        ans = N - max(cntEve.most_common()[0][1], cntOdd.most_common()[0][1])
    else:
        ans = N - max(cntEve.most_common()[0][1], cntOdd.most_common()[0][1]) - max(cntEve.most_common()[1][1], cntOdd.most_common()[1][1])
else:
    ans = N - int(cntEve.most_common()[0][1]) - int(cntOdd.most_common()[0][1])

print(ans)

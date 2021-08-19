from collections import Counter
N = int(input())
A = list(map(int, input().split()))
counter = dict(Counter(A))
four = []
tow = []
for key in counter.keys():
    if counter[key] >= 4:
        four.append(key)
        tow.append(key)
    elif counter[key] >= 2:
        tow.append(key)
if len(four) == 0 and len(tow) <= 1:
    print(0)
else:
    ans = 0
    four.sort(reverse=True)
    tow.sort(reverse=True)
    if len(four) >= 1:
        ans = max(ans, four[0] ** 2)
    if len(tow) >= 2:
        ans = max(ans, tow[1] * tow[0])
    print(ans)

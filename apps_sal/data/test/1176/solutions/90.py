n = int(input())
a = list(map(int, input().split()))

a.sort()
minus, plus = [], []

for x in a:
    if x < 0:
        minus.append(x)
    else:
        plus.append(x)

tmp = sum([abs(x) for x in a])

if len(minus) % 2 == 0:
    print(tmp)
else:
    if plus == [] or abs(minus[-1]) < plus[0]:
        print(tmp + minus[-1] * 2)
    else:
        print(tmp - plus[0] * 2)

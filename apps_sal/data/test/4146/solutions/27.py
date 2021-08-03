from collections import Counter
n = int(input())
v = list(map(int, input().split()))
a = v[1::2]
b = v[0::2]
a2 = Counter(a)
b2 = Counter(b)

if a2.most_common()[0][0] != b2.most_common()[0][0]:
    print((n - a2.most_common()[0][1] - b2.most_common()[0][1]))
else:
    if len(a2.most_common()) == len(b2.most_common()) == 1:
        print((len(a) - a2.most_common()[0][1] + len(b)))
    elif len(a2.most_common()) == 1:
        if len(b) - b2.most_common()[1][1] >= len(a) + len(b) - b2.most_common()[0][1]:
            print((len(a) + len(b) - b2.most_common()[0][1]))
        else:
            print((len(b) - b2.most_common()[1][1]))
    elif len(b2.most_common()) == 1:
        if len(a) - a2.most_common()[1][1] >= len(a) + len(b) - a2.most_common()[0][1]:
            print((len(a) + len(b) - a2.most_common()[0][1]))
        else:
            print((len(a) - a2.most_common()[1][1]))
    else:
        if len(a) - a2.most_common()[0][1] + len(b) - b2.most_common()[1][1] >= len(a) - a2.most_common()[1][1] + len(b) - b2.most_common()[0][1]:
            print((len(a) - a2.most_common()[1][1] + len(b) - b2.most_common()[0][1]))
        else:
            print((len(a) - a2.most_common()[0][1] + len(b) - b2.most_common()[1][1]))

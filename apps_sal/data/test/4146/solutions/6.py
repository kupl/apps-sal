from collections import Counter
n = int(input())
v = list(map(int, input().split()))
v0 = v[0:n - 1:2]
v1 = v[1:n:2]
V0 = Counter(v0)
V1 = Counter(v1)
if V0.most_common()[0][0] != V1.most_common()[0][0]:
    a = V0.most_common()[0][1]
    b = V1.most_common()[0][1]
else:
    if V0.most_common()[0][1] > V1.most_common()[0][1]:
        if len(V1) > 1:
            a = V0.most_common()[0][1]
            b = V1.most_common()[1][1]
        else:
            a = V0.most_common()[0][1]
            b = 0
    elif V0.most_common()[0][1] < V1.most_common()[0][1]:
        if len(V0) > 1:
            a = V1.most_common()[0][1]
            b = V0.most_common()[1][1]
        else:
            a = 0
            b = V1.most_common()[0][1]
    else:
        if len(V0) == 1 and len(V1) == 1:
            a = 0
            b = V0.most_common()[0][1]
        elif len(V0) == 1:
            a = V0.most_common()[0][1]
            b = V1.most_common()[1][1]
        elif len(V1) == 1:
            a = V0.most_common()[1][1]
            b = V1.most_common()[0][1]
        else:
            a = V0.most_common()[0][1]
            b = max(V0.most_common()[1][1], V1.most_common()[1][1])
print((n - a - b))

import math
from collections import defaultdict

total = 0
dic = defaultdict(int)
n, k = list(map(int, input().split()))
z = list(map(int, input().split()))
for ii in z:

    i = ii
    x = []
    x2 = []
    a = 2
    while a <= math.sqrt(ii):
        co = 0
        while i % a == 0:
            i = i // a
            co += 1
        co = co % k
        if co:
            x.append((a, co))
            x2.append((a, k - co))
        a += 1
    if i > 1:
        x.append((i, 1))
        x2.append((i, k - 1))
    dic[tuple(x)] += 1
    total += dic[tuple(x2)]
    if(x2 == x):
        total -= 1


print(total)

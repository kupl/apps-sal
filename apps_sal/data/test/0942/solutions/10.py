from collections import Counter

n = int(input())
a = tuple((n - int(x) for x in input().split()))
a1 = [[] for _ in range(n + 2)]
''' :type: list[list[int]] '''
b = [1] * n
for i in range(n):
    a1[a[i]].append(i)
i = 1
m = 1
for k in range(1, n + 1):
    for j in a1[k]:
        b[j] = i
        if m == k:
            m = 1
            i += 1
        else:
            m += 1
    if m != 1:
        print('Impossible')
        break
else:
    print('Possible')
    print(*b)

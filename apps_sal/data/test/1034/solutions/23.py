#!/usr/bin/env python3

x, y, z, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

# ab = []
# for i in a:
#     for j in b:
#         ab.append(i+j)
# ab.sort(reverse=True)

# ab = ab[:k]

# abc = []
# for i in ab:
#     for j in c:
#         abc.append(i+j)
# abc.sort(reverse=True)

# for i in range(k):
#     print(abc[i])

a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)

a_max = min(k, len(a))
b_max = min(k, len(b))
c_max = min(k, len(c))

abc = []
for i in range(1, k+1):
    if i > len(a):
        break
    for j in range(1, k//i+1):
        if j > len(b):
            break
        for l in range(1, k//(i*j)+1):
            if l > len(c):
                break
            # print(i, j, l)
            abc.append(a[i-1]+b[j-1]+c[l-1])

# print(abc)
# print(k)
abc.sort(reverse=True)
for i in range(k):
    print((abc[i]))


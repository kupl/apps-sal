n = int(input())
a = [int(o) for o in input().split()]
sa = [0] * n
ea = [0] * (n + 3)
oa = [0] * (n + 3)
es = 0
os = 0
for i in range(n):
    if i % 2 == 0:
        es += a[i]
        sa[i] = es
    else:
        os += a[i]
        sa[i] = os
    oa[i] = os
    ea[i] = es
count = 0
for i in range(n):
    if i % 2 == 0:
        if es - ea[i] + oa[i - 1] == os - oa[i - 1] + ea[i - 1]:
            count += 1
    elif os - oa[i] + ea[i - 1] == es - ea[i - 1] + oa[i - 1]:
        count += 1
print(count)

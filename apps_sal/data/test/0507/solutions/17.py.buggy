n = int(input())
a = input().split()
b = input().split()
a = [int(i) for i in a]
b = [int(i) for i in b]

counter = [-1 for i in range(n)]

k_a = 0
k_a_i1, k_a_i2 = -1, -1

for i in range(n):
    if counter[a[i] - 1] != -1:
        k_a = a[i]
        k_a_i1, k_a_i2 = counter[a[i] - 1], i
    counter[a[i] - 1] = i
g_a = counter.index(-1) + 1

counter = [-1 for i in range(n)]

k_b = 0
k_b_i1, k_b_i2 = -1, -1

for i in range(n):
    if counter[b[i] - 1] != -1:
        k_b = b[i]
        k_b_i1, k_b_i2 = counter[b[i] - 1], i
    counter[b[i] - 1] = i

g_b = counter.index(-1) + 1

res = a.copy()
res[k_a_i1] = g_a

c_a = 0
c_b = 0

for i in range(n):
    if res[i] != a[i]:
        c_a += 1
    if res[i] != b[i]:
        c_b += 1

if c_a == 1 and c_b == 1:
    out = ''
    for i in res:
        out += str(i) + ' '
    print(out)
    return

res = a.copy()
res[k_a_i2] = g_a

c_a = 0
c_b = 0

for i in range(n):
    if res[i] != a[i]:
        c_a += 1
    if res[i] != b[i]:
        c_b += 1

if c_a == 1 and c_b == 1:
    out = ''
    for i in res:
        out += str(i) + ' '
    print(out)
    return

res = a.copy()
res[k_b_i1] = g_b

c_a = 0
c_b = 0

for i in range(n):
    if res[i] != a[i]:
        c_a += 1
    if res[i] != b[i]:
        c_b += 1

if c_a == 1 and c_b == 1:
    out = ''
    for i in res:
        out += str(i) + ' '
    print(out)
    return

res = a.copy()
res[k_b_i2] = g_b

c_a = 0
c_b = 0

for i in range(n):
    if res[i] != a[i]:
        c_a += 1
    if res[i] != b[i]:
        c_b += 1

if c_a == 1 and c_b == 1:
    out = ''
    for i in res:
        out += str(i) + ' '
    print(out)
    return

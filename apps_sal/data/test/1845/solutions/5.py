n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()
p = sum(arr)
a = []
d = {}
for i in range(1, 101):
    d[i] = 0
for i in arr:
    d[i] += 1
for i in range(1, 101):
    for j in range(1, 101):
        if j % i == 0:
            for k in range(1, 101):
                a.append((j, k, k + j - j // i - k * i))
m = -100000000
for i in a:
    if i[0] == i[1]:
        if d[i[0]] >= 2:
            m = max(m, i[2])
    elif d[i[0]] != 0 and d[i[1]] != 0:
        m = max(m, i[2])
print(p - m)

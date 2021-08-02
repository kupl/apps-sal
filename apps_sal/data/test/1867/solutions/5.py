n = int(input())

arr = list(map(int, input().split()))

d = {}

for i in range(n):
    if arr[i] not in d:
        d[arr[i]] = (i, i, 1)
    else:
        x = d[arr[i]]
        y = (x[0], i, x[2] + 1)
        d[arr[i]] = y

# print(d)

p = 10**20
r = 0

for i in d:
    m = d[i]
    if(m[2] > r):
        r = m[2]
        p = m[1] - m[0]
        q = m[0], m[1]
    elif(m[2] == r and (m[1] - m[0]) < p):
        r = m[2]
        p = m[1] - m[0]
        q = (m[0], m[1])

print(q[0] + 1, q[1] + 1)

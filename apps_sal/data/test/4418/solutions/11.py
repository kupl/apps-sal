input()  # discard n
num = [4, 8, 15, 16, 23, 42]
prev = {i: j for i, j in zip(num[1:], num)}
c = {v: 0 for v in num}
n = 0
for a in map(int, input().split()):
    #print('before', a, c)
    if a == num[0]:  # first
        c[a] += 1
    else:
        if c[prev[a]]:
            c[prev[a]] -= 1
            if a != num[-1]: c[a] += 1
        else: n += 1  # waste
    #print('after', a, c)

# print(c)
for i, v in enumerate(num):
    # print(i,v,c[v])
    n += (i + 1) * c[v]

print(n)

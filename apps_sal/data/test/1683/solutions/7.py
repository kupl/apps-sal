import math

n = int(input())

arr = [i for i in input().split()]


CT = [0 for i in range(40)]
for i in arr:
    CT[len(i)] += 1


P = [0 for i in range(40)]
M = 998244353
ans = 0

howmanyhavelengthlesser = [0 for i in range(40)]
howmanyhavelengthgreater = [0 for i in range(40)]

for i in range(40):
    for j in range(i):
        howmanyhavelengthlesser[i] += CT[j]
    for j in range(i + 1, 40):
        howmanyhavelengthgreater[i] += CT[j]

# second

for i in arr:
    cur = 0
    for j in range(len(i) - 1, -1, -1):
        for k in range(cur, 2 * cur + 1):
            if (k != 2 * cur):
                P[k] += int(i[j]) * (CT[cur - (2 * cur - k)])  # >something
            else:
                #print (i[j],k,cur,howmanyhavelengthgreater[cur]+CT[cur])
                P[k] += int(i[j]) * (howmanyhavelengthgreater[cur] + CT[cur])  # >something
        cur += 1


# first

for i in arr:
    cur = 0
    for j in range(len(i) - 1, -1, -1):
        for k in range(cur + 1, 2 * cur + 2):
            if(k == 2 * cur + 1): P[k] += int(i[j]) * (howmanyhavelengthgreater[cur + 1] + CT[cur + 1])  # >something
            else: P[k] += int(i[j]) * (CT[cur + 1 - (2 * cur + 1 - k)])  # >something
        cur += 1
    # print(P)


for i in range(30):
    ans = (ans + P[i] * pow(10, i, M)) % M;
print(ans)

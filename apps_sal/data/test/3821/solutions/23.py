import sys
n = int(input()) 
index = [i for i in range(n)]
tmp = list(map(float, sys.stdin.readline().split()))
ans = []
maxP = 0
while len(index):
    j = 0
    ma = 0
    for k in index:
        if tmp[k] >= ma:
            ma = tmp[k]
            j = k
    index.remove(j)
    ans.append(tmp[j])
    tp = 0
    for i in range(len(ans)):
        q  = ans[i]
        for k in range(len(ans)):
            if i != k:
                q *= 1 - ans[k]
        tp += q
    if tp > maxP:
        maxP = tp
    else:
        ans.remove(tmp[j])

print("{0:.9f}".format(maxP))



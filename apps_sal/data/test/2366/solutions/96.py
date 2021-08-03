n = int(input())
a = list(map(int, input().split()))

numdict = {}

for n in a:
    if n in numdict.keys():
        numdict[n] += 1
    else:
        numdict[n] = 1

all_sum = 0
for k in numdict.keys():
    v = numdict[k]
    all_sum += (v * (v - 1)) // 2

for n in a:
    print(all_sum - numdict[n] + 1)

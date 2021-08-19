from collections import defaultdict
count = 0
input()
L = list(map(int, input().strip().split()))
PoT = [2 ** i for i in range(31)]
dic = defaultdict(int)
for x in L:
    dic[x] += 1
for x in L:
    for y in PoT:
        if y - x in list(dic.keys()):
            if x == y - x and dic[x] == 1:
                pass
            else:
                break
    else:
        count += 1
print(count)

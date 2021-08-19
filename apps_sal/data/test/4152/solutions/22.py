from collections import defaultdict
counter = 0
n = int(input())
List = list(map(int, input().strip().split()))
List = list(List)
PofT = [2 ** i for i in range(31)]
dic = defaultdict(int)
for x in List:
    dic[x] += 1
for x in List:
    for y in PofT:
        if y - x in list(dic.keys()):
            if x == y - x and dic[x] == 1:
                pass
            else:
                break
    else:
        counter += 1
print(counter)

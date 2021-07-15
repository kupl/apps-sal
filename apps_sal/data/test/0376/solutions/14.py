
import random
n = int(input())
strengths = list(map(int,input().split()))
l = [[] for i in range(n)]
for j in range(n-1):
    a,b = list(map(int,input().split()))
    l[a-1].append(b-1)
    l[b-1].append(a-1)
hacked = max(strengths)
greatest_value = sum(i==hacked for i in strengths)
result = hacked
if greatest_value == 1:
    computer = strengths.index(result)
    adjlist = set(l[computer])
    adjlist.add(computer)
    for i in range(n):
        if i in adjlist:
            continue
        if strengths[i] == hacked - 1:
            result += 1
            break
else:
    for i in range(n):
        count = 0
        if strengths[i] == hacked:
            count += 1
        for v in l[i]:
            if strengths[v] == hacked:
                count += 1
        if count == greatest_value:
            result += 1
            break
    else:
        result += 2
print (result)



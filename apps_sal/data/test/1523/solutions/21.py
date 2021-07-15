a = list(map(int, input().split()))
idlers = a[0]
jobs = a[1]
choices = list(map(int, input().split()))
persuade = list(map(int, input().split()))
count_rep = []
count = {}
for i in range(len(choices)):
    if choices[i] not in count:
        count[choices[i]] = 1
    else:
        count_rep.append(choices[i])
count_rep_set = set(count_rep)
pers = {}
for j in count_rep_set:
    pers[j] = []
for k in range(len(choices)):
    if choices[k] in count_rep_set:
        pers[choices[k]].append(persuade[k])
mergedList = []
for key in pers.keys():
    pers[key].sort()
    pers[key].pop()
    mergedList += pers[key]
mergedList.sort()
num = jobs - len(set(choices))
sum = 0
for l in range(num):
    sum += mergedList[l]
print(sum)

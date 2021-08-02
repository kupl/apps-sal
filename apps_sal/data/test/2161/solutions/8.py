from sys import stdin, stdout

n = int(stdin.readline().rstrip())
nameDict = {}
for _ in range(n):
    s = stdin.readline().rstrip().split()
    name = s[0]
    if name not in nameDict:
        nameDict[name] = set()
    for number in s[2:]:
        nameDict[name].add(number)

for name in list(nameDict.keys()):
    rem = set()
    for no1 in nameDict[name]:
        for no2 in nameDict[name]:
            if no1 == no2:
                continue
            l1 = len(no1)
            l2 = len(no2)
            if l1 < l2 and no2[-l1:] == no1:
                rem.add(no1)
    for no in rem:
        nameDict[name].remove(no)

print(len(list(nameDict.keys())))
for name in list(nameDict.keys()):
    print(' '.join([name, str(len(nameDict[name]))] + list(nameDict[name])))

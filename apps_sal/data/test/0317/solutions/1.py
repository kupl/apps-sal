n = int(input())
s = input()
mySet = set()
for c in s:
    mySet.add(c.lower())
if len(mySet) == 26:
    print('YES')
else:
    print('NO')

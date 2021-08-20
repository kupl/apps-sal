def compare(s1, s2):
    ind = False
    for i in range(max(len(s1), len(s2))):
        if s1[i] > s2[i]:
            ind = True
            return 's1'
        elif s2[i] > s1[i]:
            ind = True
            return 's2'
    if len(s1) > len(s2):
        return 's1'
    elif len(s1) < len(s2):
        return 's2'
    else:
        return 'False'


n = int(input())
L = [input() for i in range(n)]
first = []
second = []
for s in L:
    if s[0] == '-':
        second.append(int(s) * -1)
    else:
        first.append(int(s))
if sum(first) > sum(second):
    print('first')
elif sum(first) < sum(second):
    print('second')
else:
    res = compare(first, second)
    if res == 's1':
        print('first')
    elif res == 's2':
        print('second')
    elif int(L[-1]) >= 0:
        print('first')
    else:
        print('second')

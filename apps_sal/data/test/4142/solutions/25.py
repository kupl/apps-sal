s = [i for i in input()]
s_len = len(s)
list1 = []
list2 = []
for j in range(0, s_len, 2):
    for even in s[j]:
        list1.append(even in ['R', 'U', 'D'])
for k in range(1, s_len, 2):
    for odd in s[k]:
        list2.append(odd in ['L', 'U', 'D'])

if False in list1:
    print('No')
elif False in list2:
    print('No')
else:
    print('Yes')

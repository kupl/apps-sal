S = input()
count = 0
list1 = ''
list2 = ''
if S[0] == 'A':
    count += 1
if S[2:-1].count('C') == 1:
    count += 1
for n in S:
    if n == 'A' or n == 'C':
        list1 += n
    else:
        list2 += n
if list2.islower():
    count += 1
if count == 3:
    print('AC')
else:
    print('WA')

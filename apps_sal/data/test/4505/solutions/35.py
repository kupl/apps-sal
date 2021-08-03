S = input()
a_list = list(S)
a_ct = 0
b_ct = 0
c_ct = 0

for i in range(0, 3):
    if a_list[i] == 'a':
        a_ct = a_ct + 1

for i in range(0, 3):
    if a_list[i] == 'b':
        b_ct = b_ct + 1

for i in range(0, 3):
    if a_list[i] == 'c':
        c_ct = c_ct + 1

if a_ct == 1 and b_ct == 1 and c_ct == 1:
    print('Yes')
else:
    print('No')

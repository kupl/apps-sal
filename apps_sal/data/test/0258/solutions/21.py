o = input()
inp = input()
count_1 = 0
sum_1 = 0
count_2 = 0
sum_2 = 0
for i in range(len(inp) // 2):
    if inp[i] == '?':
        count_1 += 1
    else:
        sum_1 += int(inp[i])
for j in range(len(inp) // 2):
    i = len(inp) // 2 + j
    if inp[i] == '?':
        count_2 += 1
    else:
        sum_2 += int(inp[i])
if sum_2 - sum_1 == 9 * (count_1 - count_2) // 2:
    print('Bicarp')
else:
    print('Monocarp')

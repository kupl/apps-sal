Bingo_1 = list(map(int, input().split()))
Bingo_2 = list(map(int, input().split()))
Bingo_3 = list(map(int, input().split()))
number_table = []
number_count = int(input())
for i in range(number_count):
    number_table.append(int(input()))
for j in range(number_count):
    if number_table[j] == Bingo_1[0]:
        Bingo_1[0] = 0
    elif number_table[j] == Bingo_1[1]:
        Bingo_1[1] = 0
    elif number_table[j] == Bingo_1[2]:
        Bingo_1[2] = 0
    elif number_table[j] == Bingo_2[0]:
        Bingo_2[0] = 0
    elif number_table[j] == Bingo_2[1]:
        Bingo_2[1] = 0
    elif number_table[j] == Bingo_2[2]:
        Bingo_2[2] = 0
    elif number_table[j] == Bingo_3[0]:
        Bingo_3[0] = 0
    elif number_table[j] == Bingo_3[1]:
        Bingo_3[1] = 0
    elif number_table[j] == Bingo_3[2]:
        Bingo_3[2] = 0
if Bingo_1[0] == 0 and Bingo_1[1] == 0 and (Bingo_1[2] == 0):
    print('Yes')
elif Bingo_2[0] == 0 and Bingo_2[1] == 0 and (Bingo_2[2] == 0):
    print('Yes')
elif Bingo_3[0] == 0 and Bingo_3[1] == 0 and (Bingo_3[2] == 0):
    print('Yes')
elif Bingo_1[0] == 0 and Bingo_2[0] == 0 and (Bingo_3[0] == 0):
    print('Yes')
elif Bingo_1[1] == 0 and Bingo_2[1] == 0 and (Bingo_3[1] == 0):
    print('Yes')
elif Bingo_1[2] == 0 and Bingo_2[2] == 0 and (Bingo_3[2] == 0):
    print('Yes')
elif Bingo_1[0] == 0 and Bingo_2[1] == 0 and (Bingo_3[2] == 0):
    print('Yes')
elif Bingo_1[2] == 0 and Bingo_2[1] == 0 and (Bingo_3[0] == 0):
    print('Yes')
else:
    print('No')

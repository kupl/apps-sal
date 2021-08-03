s = input().split()
l = sum([int(i) for i in s])
pos = [0, 0, 0]
ls = []
for j in range(3):
    ls += [[int(i) for i in input().split()]]
    ls[j] += [100100]
    ls[j].sort()

shet = [0, 0, 0]
bot_ind = 0
top_granica = 0
summa = 0
i = 0
main_list = []
kandidat = []
while i < l:
    if ls[0][shet[0]] < ls[1][shet[1]]:
        if ls[0][shet[0]] < ls[2][shet[2]]:
            kandidat = [ls[0][shet[0]], 0]
        else:
            kandidat = [ls[2][shet[2]], 2]
    else:
        if ls[1][shet[1]] < ls[2][shet[2]]:
            kandidat = [ls[1][shet[1]], 1]
        else:
            kandidat = [ls[2][shet[2]], 2]
    if bot_ind == i:
        main_list += [kandidat]
        shet[kandidat[1]] += 1
        top_granica = main_list[bot_ind][0] * 2

        pos[kandidat[1]] += 1
    else:
        if kandidat[0] > top_granica:
            if pos[0] > 0 and pos[1] > 1 and pos[2] > 2:
                pos[main_list[bot_ind][1]] -= 1
                if not main_list[bot_ind][1]:
                    summa += pos[1] * (pos[1] - 1) * pos[2] * (pos[2] - 1) * (pos[2] - 2) // 12
                elif main_list[bot_ind][1] == 1:
                    summa += pos[0] * pos[1] * pos[2] * (pos[2] - 1) * (pos[2] - 2) // 6
                else:
                    summa += pos[0] * pos[1] * (pos[1] - 1) * pos[2] * (pos[2] - 1) // 4
                bot_ind += 1
                top_granica = main_list[bot_ind][0] * 2
            else:
                pos[main_list[bot_ind][1]] -= 1
                bot_ind += 1
                if bot_ind < i:
                    top_granica = main_list[bot_ind][0] * 2
            i -= 1

        else:
            main_list += [kandidat]
            shet[kandidat[1]] += 1
            pos[kandidat[1]] += 1
    i += 1
while pos[0] > 0 and pos[1] > 1 and pos[2] > 2:
    pos[main_list[bot_ind][1]] -= 1
    if not main_list[bot_ind][1]:
        summa += pos[1] * (pos[1] - 1) * pos[2] * (pos[2] - 1) * (pos[2] - 2) // 12
    elif main_list[bot_ind][1] == 1:
        summa += pos[0] * pos[1] * pos[2] * (pos[2] - 1) * (pos[2] - 2) // 6
    else:
        summa += pos[0] * pos[1] * (pos[1] - 1) * pos[2] * (pos[2] - 1) // 4
    bot_ind += 1


print(summa)

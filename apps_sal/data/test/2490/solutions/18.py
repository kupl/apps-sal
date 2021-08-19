n = str(input())
n_list = list(reversed(n))
n_list.append('0')
sum = 0
kuriagari = False
for i in range(len(n_list)):
    num = int(n_list[i])
    if kuriagari:
        num += 1
        kuriagari = False
    if num == 10:
        num = 0
        kuriagari = True
    if num < 5:
        sum += num
    elif num > 5:
        sum += 10 - num
        kuriagari = True
    else:
        sum += 5
        if int(n_list[i + 1]) >= 5:
            kuriagari = True
print(sum)

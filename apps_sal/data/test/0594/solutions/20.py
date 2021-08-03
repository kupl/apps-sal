num = input().rstrip('\n').split(' ')
correct_solution = input().rstrip('\n').split(' ')
wrong_solution = input().rstrip('\n').split(' ')

n = int(num[0])
m = int(num[1])


def toIntList(list):
    newlist = []
    for k in list:
        newlist.append(int(k))
    return newlist


correct_time = toIntList(correct_solution)
correct_time.sort()
wrong_time = toIntList(wrong_solution)
wrong_time.sort()

if correct_time[-1] >= wrong_time[0]:
    print(-1)
elif correct_time[0] * 2 >= wrong_time[0]:
    print(-1)
else:
    print(max(correct_time[-1], correct_time[0] * 2))

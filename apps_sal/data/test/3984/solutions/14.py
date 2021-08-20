l = input()
mini = 1000000
for i in range(len(l)):
    if ord(l[i]) > mini:
        print('Ann')
    else:
        print('Mike')
    mini = min(mini, ord(l[i]))

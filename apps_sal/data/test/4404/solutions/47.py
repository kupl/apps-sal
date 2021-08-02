date = input()
list_date = date.split('/')
if int(list_date[0]) <= 2018:
    print('Heisei')
elif int(list_date[0]) <= 2019 and int(list_date[1]) <= 4:
    print('Heisei')
else:
    print('TBD')

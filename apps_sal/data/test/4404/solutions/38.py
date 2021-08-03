y, m, d = map(int, input().split('/'))

if(y < 2019):

    print('Heisei')

elif(y == 2019):

    if(m < 5):
        print('Heisei')
    else:
        print('TBD')

else:

    print('TBD')

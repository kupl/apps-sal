d = int(input())

l1 = [22, 23, 24, 25]

dic = {22: 'Christmas Eve Eve Eve',
       23: 'Christmas Eve Eve',
       24: 'Christmas Eve',
       25: 'Christmas'}

for i in range(4):
    if(l1[i] == d):
        print(dic[l1[i]])

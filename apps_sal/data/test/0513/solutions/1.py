#f = open('data.txt')
lists=[]
dicts={}
sets = set()

for i in range(8):
    lists.append(tuple(input().split()))
'''for x in f:
    lists.append(tuple(x.split()))'''
for x in lists:
    sets.add(x)
    
if len(sets) == 8:
    for x in range(8):
        count = dicts.get(int(lists[x][0]),0)
        dicts[int(lists[x][0])] = count+1

    if len(list(dicts.keys()))==3:
        temp = sorted(dicts.items())
        if temp[0][1]==3 and temp[1][1] == 2 and temp[2][1] ==3:
            dicts.clear()
            for x in range(8):
                count = dicts.get(int(lists[x][1]),0)
                dicts[int(lists[x][1])] = count+1
            if len(list(dicts.keys()))==3:
                temp = sorted(dicts.items())
                if temp[0][1]==3 and temp[1][1] == 2 and temp[2][1] ==3:
                    print('respectable')
                else:
                    print('ugly')
            else:
                print('ugly')
        else:
            print('ugly')

    else:
        print('ugly')
else:
    print('ugly')


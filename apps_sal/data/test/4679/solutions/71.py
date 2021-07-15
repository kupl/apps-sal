sa = input().replace('a', '0').replace('b', '1').replace('c', '2')
sb = input().replace('a', '0').replace('b', '1').replace('c', '2')
sc = input().replace('a', '0').replace('b', '1').replace('c', '2')
sl = [sa, sb, sc]
abc = ['A', 'B',' C']
turn = 0

while True:
    if len(sl[turn]) == 0:
        print(abc[turn])
        return
    else:
        sl[turn], turn = sl[turn][1:], int(sl[turn][0])

print(sl)

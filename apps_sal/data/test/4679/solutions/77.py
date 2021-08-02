SA = list(input())
SB = list(input())
SC = list(input())

x = 'a'

while True:
    if x == 'a':
        if len(SA) == 0:
            print('A')
            return
        x = SA[0]
        SA.remove(x)
    if x == 'b':
        if len(SB) == 0:
            print('B')
            return
        x = SB[0]
        SB.remove(x)
    if x == 'c':
        if len(SC) == 0:
            print('C')
            return
        x = SC[0]
        SC.remove(x)

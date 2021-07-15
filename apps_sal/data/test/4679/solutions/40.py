def main():
    SA = list(input())
    SB = list(input())
    SC = list(input())

    SA.reverse()
    SB.reverse()
    SC.reverse()

    turn = 'a'
    for i in range(400):
        if turn == 'a':
            if len(SA) == 0:
                print('A')
                return
            turn = SA.pop()
        elif turn == 'b':
            if len(SB) == 0:
                print('B')
                return
            turn = SB.pop()
        else:
            if len(SC) == 0:
                print('C')
                return
            turn = SC.pop()
 
def __starting_point():
    main()

__starting_point()

import re
Fe = re.compile('.*lala\.!')
FeA = "Freda's"
Ra = re.compile('miao\..*')
RaA = "Rainbow's"
NotSure = "OMG>.< I don't know!"


def __starting_point():
    N = int(input())
    for times in range(N):
        inp = input()
        inp = inp.strip('\n') + '!'

        f1 = Fe.match(inp) != None
        f2 = Ra.match(inp) != None

        if f1:
            if f2:
                print(NotSure)
            else:
                print(FeA)
        elif f2:
            print(RaA)
        else:
            print(NotSure)


__starting_point()

x, y = {}, {}

def get_len(path):
    return int(len(path[1]))

x['A'] = input()
x['B'] = input()
x['C'] = input()
x['D'] = input()

y = sorted(list(x.items()), key=get_len)

if (len(y[0][1]) - 2) * 2 <= (len(y[1][1]) - 2) and (len(y[3][1]) - 2) < (len(y[2][1]) - 2) * 2:
    print( y[0][0] )
elif (len(y[3][1]) - 2) >= (len(y[2][1]) - 2) * 2 and (len(y[0][1]) - 2) * 2 > (len(y[1][1]) - 2):
    print( y[3][0] )
else:
    print( "C" )


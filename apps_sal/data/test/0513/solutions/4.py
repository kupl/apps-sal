class Point:
    def __init__(self, x_p, y_p):
        self.x = x_p
        self.y = y_p
        

points = []
sub_x = []
sub_y = []
key = False
for i in range(8):
    x, y = list(map(int, input().split()))
    if ([x, y] in points):
        key = True
    if x not in sub_x:
        sub_x.append(x)
    if y not in sub_y:
        sub_y.append(y)
    points.append([x, y])
sub_x.sort()
sub_y.sort()
if (key):
    print('ugly')
else:
    if (len(sub_x) == 3) and (len(sub_y) == 3):
        if ([sub_x[1], sub_y[1]] in points):
            print('ugly')
        else:
            print('respectable')
    else:
        print('ugly')


import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    x = input()
    y = input()
    pos_y = y.rfind('1')
    d = len(y) - pos_y - 1
    if d != 0:
        pos_x = x[:-d].rfind('1')
    else:
        pos_x = x.rfind('1')
    pos_x = -len(x) + pos_x
    pos_y = -len(y) + pos_y
    k = pos_y - pos_x
    print(k)

# 1: starting from there, P1 wins (who starts)
# 0: P0 wins (who doesn't start)
#
# 0 0 1 1 1 1 1
# 0 0 0 1 1
# 1 0 0 0
# 1 1 0
# 1 1
# 1
# 1
# |X-Y| <= 1 : 0
# |X-Y| >  1 : 1
# X-Y: must change by 3
X, Y = list(map(int, input().split()))
if abs(X - Y) > 1:
    print('Alice')
else:
    print('Brown')

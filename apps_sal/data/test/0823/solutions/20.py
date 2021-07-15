'''l = [[(0, 0), (1, 0)],
     [(1, 0), (1, 1)],
     [(1, 1), (-1, 1)],
     [(-1, 1), (-1, -1)],
     [(-1, - 1), (2, -1)],
     [(2, -1), (2, 2)]]
'''
'''
pattern er shudhone na paria
last e net theke copy marcha
pattern copy marcha re.
'''
x,y = list(map(int, input().split()))
if y >= x and y < -x:
    print(-4*x-1)
elif y > x and y >= -x:
    print(4*y-2)
elif y <= x and y > 1-x:
    print(4*x-3)
elif y < x and y <= 1-x:
    print(-4*y)
else:
    print(0)


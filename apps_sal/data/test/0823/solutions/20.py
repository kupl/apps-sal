"""l = [[(0, 0), (1, 0)],
     [(1,\u20090),\u2009(1,\u20091)],
     [(1,\u20091),\u2009(-1,\u20091)],
     [(-1,\u20091),\u2009(-1,\u2009-1)],
     [(-1,\u2009-\u20091),\u2009(2,\u2009-1)],
     [(2,\u2009-1),\u2009(2,\u20092)]]
"""
'\npattern er shudhone na paria\nlast e net theke copy marcha\npattern copy marcha re.\n'
(x, y) = list(map(int, input().split()))
if y >= x and y < -x:
    print(-4 * x - 1)
elif y > x and y >= -x:
    print(4 * y - 2)
elif y <= x and y > 1 - x:
    print(4 * x - 3)
elif y < x and y <= 1 - x:
    print(-4 * y)
else:
    print(0)

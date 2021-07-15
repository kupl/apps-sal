import sys
colors = input()
finish_colors = input()
result = 0
differnt_finish_colors = set(finish_colors)
tested_colors = []
for color in differnt_finish_colors:
    if not (color in tested_colors):
        if not colors.count(color):
            print('-1')
            return
        else:
            result += min([colors.count(color), finish_colors.count(color)])
print(result)

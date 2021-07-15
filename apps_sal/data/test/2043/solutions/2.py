__author__ = 'Руслан'
name = input()
finder = input()
left_pos = 0
right_pos = len(finder)
isfind = True
for i in name:
    left_pos = finder.find(i, left_pos)
    if left_pos == -1:
        isfind = False
        break
    else:
        left_pos += 1


if isfind:
    for i in name[::-1]:
        right_pos = finder.rfind(i, 0, right_pos)

if right_pos >= left_pos and isfind:
    print(right_pos - left_pos+1)
else:
    print(0)

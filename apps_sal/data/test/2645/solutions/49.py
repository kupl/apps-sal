s = input()
gu = 1
pa = 0
point = 0
if s[0] == 'p':
    point -= 1
for hand in s[1:]:
    if hand == 'g':
        if pa < gu:
            point += 1
            pa += 1
        else:
            gu += 1
    elif hand == 'p':
        if pa < gu:
            pa += 1
        else:
            gu += 1
            point -= 1
print(point)

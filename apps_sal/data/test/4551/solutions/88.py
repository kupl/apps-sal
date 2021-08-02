lst = input().split()

d = (int(lst[0]) + int(lst[1])) - (int(lst[2]) + int(lst[3]))

if d == 0:
    print('Balanced')
elif 0 < d:
    print('Left')
else:
    print('Right')

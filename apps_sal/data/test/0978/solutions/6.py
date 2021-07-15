k = int(input())

panels = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
flag = True

for i in range(4):
    line = input()
    for ch in line:
        if ch == '.' :
            continue
        panels[ch] += 1

v = list(panels.values())

for i in v:
    if i > 2 * k:
        flag = False #print('NO')

#print(panels)
if flag :
    print('YES')
else:
    print('NO')


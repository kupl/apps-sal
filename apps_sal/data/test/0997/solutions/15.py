s = input()
s = s.replace(',', ';')
s = s.split(';')
(ans1, ans2) = ([], [])
for elem in s:
    if len(elem) > 0:
        if elem == '0' or elem[0] != '0':
            try:
                x = int(elem)
                ans1.append(x)
            except:
                ans2.append(elem)
        else:
            ans2 += [elem]
    else:
        ans2 += ['']
if ans1:
    print('"', end='')
    print(*ans1, sep=',', end='"\n')
else:
    print('-')
if ans2:
    print('"', end='')
    print(*ans2, sep=',', end='"\n')
else:
    print('-')

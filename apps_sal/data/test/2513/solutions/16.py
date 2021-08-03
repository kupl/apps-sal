n = int(input())
s = input()
s += s[0]
d = {'S': 'W', 'W': 'S'}
flag = True
for sw in ['SS', 'WW', 'SW', 'WS']:
    l = sw
    for i in range(1, n + 1):
        if l[i] == 'S' and s[i] == 'o' or l[i] == 'W' and s[i] == 'x':
            l += l[i - 1]
        else:
            l += d[l[i - 1]]
    if l[0] == l[-2] and l[1] == l[-1]:
        print((l[:-2]))
        flag = False
        break
if flag:
    print((-1))

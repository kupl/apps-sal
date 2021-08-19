list1 = list()
cmd = input()
i = 0
n = len(cmd)
while i < len(cmd) and i != -1:
    x = cmd[i]
    if x == '"':
        ind = cmd.find('"', i + 1, n)
        if ind == -1:
            break
        if ind + 1 < len(cmd) and cmd[ind + 1] == ' ':
            list1.append(cmd[i + 1:ind])
        else:
            ind = cmd.find('"', ind + 1, n)
            list1.append(cmd[i + 1:ind])
        i = ind + 1
        if ind == -1:
            break
    elif x != ' ':
        j = i
        while i < n and cmd[i] != ' ':
            i += 1
        x = cmd[j:i]
        list1.append(x)
        i += 1
    else:
        i += 1
for x in list1:
    print('<', x, '>', sep='')

a = input()
inp = input()
a = []
ans = ""
for i in range(len(inp)):
    if (i < len(a)):
        continue
    if (inp[i] != 'a' and inp[i] != 'e' and inp[i] != 'i' and inp[i] != 'o' and inp[i] != 'u' and inp[i] != 'y'):
        a.append(1)
        continue
    if (i <= len(inp) - 3 and inp[i] == inp[i + 1] and inp[i] == inp[i + 2]):
        a.append(1)
        for k in range(i + 1, len(inp)):
            if (inp[k] == inp[k - 1]):
                a.append(0)
            else:
                break
        continue
    if (i <= len(inp) - 3 and inp[i] == inp[i + 1] and inp[i] != inp[i + 2]):
        if (inp[i] == 'o' or inp[i] == 'e'):
            a.append(1)
            a.append(1)
            continue
        else:
            a.append(1)
            a.append(0)
            continue
    elif (i == len(inp) - 2):
        if (inp[i] == inp[i + 1] and inp[i] != 'o' and inp[i] != 'e'):
            a.append(1)
            a.append(0)
        else:
            a.append(1)
            a.append(1)
        break
    a.append(1)

ans = ""
for i in range(len(a)):
    if (a[i] == 1):
        ans += inp[i]
print(ans)

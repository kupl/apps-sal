s = list(input())
ans = list()
for i in s:
    if i == '0':
        ans.append(0)
    elif i == '1':
        ans.append(1)
    else:
        try:
            ans.pop(-1)
        except:
            pass
for i in ans:
    print(i, end='')
print()

s = input()
ans = []

for i in s:
    if i == 'B':
        if ans != []:
            ans.pop(-1)
    else:
        ans.append(i)
print(''.join(ans))

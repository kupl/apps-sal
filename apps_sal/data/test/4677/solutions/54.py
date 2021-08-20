s = [ss for ss in str(input())]
ans = []
for i in s:
    if i == '0' or i == '1':
        ans.append(i)
    elif len(ans) > 0:
        ans.pop(-1)
print(''.join(ans))

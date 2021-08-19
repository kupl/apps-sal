s = input()
ans = []
for i in s:
    if i == '0' or i == '1':
        ans.append(i)
    elif len(ans):
        ans.pop()
print(''.join(ans))

s = input()
ans = []
for i in s:
    if i == '0':
        ans.append(0)
    elif i == '1':
        ans.append(1)
    elif len(ans) != 0:
        ans.pop(-1)
print(*ans, sep='')

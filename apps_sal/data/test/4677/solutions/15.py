a = list(input())
ans = []
for i in range(len(a)):
    if a[i] == '0':
        ans.append('0')
    elif a[i] == '1':
        ans.append('1')
    elif a[i] == 'B':
        if ans == []:
            continue
        else:
            ans.pop(-1)
print(''.join(ans))

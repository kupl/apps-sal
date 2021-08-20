key = list(input())
ans = []
for i in key:
    if i == '0' or i == '1':
        ans.append(i)
    elif len(ans) == 0:
        continue
    else:
        del ans[-1]
print(''.join(ans))

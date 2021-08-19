arr = list(map(int, input().split()))
n = int(input())
d = {'S': 0, 'M': 1, 'L': 2, 'XL': 3, 'XXL': 4, 'XXXL': 5, 0: 'S', 1: 'M', 2: 'L', 3: 'XL', 4: 'XXL', 5: 'XXXL'}
ans = [-1] * n
fl = False
men = []
for i in range(n):
    s = input().split(',')
    if len(s) == 1:
        if arr[d[s[0]]] != 0:
            arr[d[s[0]]] -= 1
            ans[i] = s[0]
        else:
            print('NO')
            fl = True
    else:
        men.append((d[s[0]], d[s[1]], i))
if not fl:
    men.sort()
    # print(men)
    for i in range(len(men)):
        if arr[men[i][0]] != 0:
            arr[men[i][0]] -= 1
            ans[men[i][-1]] = d[men[i][0]]
            continue
        elif len(men[i]) == 2:
            print('NO')
            fl = True
            break
        elif arr[men[i][1]] != 0:
            arr[men[i][1]] -= 1
            ans[men[i][-1]] = d[men[i][1]]
            continue
        else:
            print('NO')
            fl = True
            break

    if not fl:
        print('YES')
        print('\n'.join(ans))

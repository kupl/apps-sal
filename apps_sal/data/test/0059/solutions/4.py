n = int(input())
a = list(map(int, input().split()))
s = input()
temp = []
mini = n + 1
maxi = -1
for i in range(n - 1):
    if s[i] == '1':
        mini = min(mini, a[i])
        maxi = max(maxi, a[i])
    elif i != 0 and s[i - 1] == '1':
        mini = min(mini, a[i])
        maxi = max(maxi, a[i])
        temp.append(mini)
        temp.append(maxi)
        mini = n + 1
        maxi = -1
    else:
        temp.append(a[i])
if mini != n + 1:
    mini = min(mini, a[-1])
    maxi = max(maxi, a[-1])
    temp.append(mini)
    temp.append(maxi)
else:
    temp.append(a[-1])
for i in range(1, len(temp)):
    if temp[i] < temp[i - 1]:
        print('NO')
        break
else:
    print('YES')

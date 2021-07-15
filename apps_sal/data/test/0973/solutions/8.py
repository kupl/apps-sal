r, c = map(int, input().split())
num = [[1] * (c + 2)]
for i in range(r):
    s = input()
    ans = [1]
    for j in range(len(s)):
        if s[j] == '.':
            ans.append('D')
        else:
            ans.append(s[j])
    ans.append(1)
    num.append(ans)
num.append([1] * (c + 2))
fl = True
for i in range(1, len(num) - 1):
    for j in range(1, len(num[i]) - 1):
        if num[i][j] == 'S' and (num[i][j - 1]== 'W' or num[i][j + 1]== 'W' or num[i - 1][j]== 'W' or num[i + 1][j]== 'W'):
            fl = False
if fl:
    print('Yes')
    for i in range(1, len(num) - 1):
        for j in range(1, len(num[i]) - 1):
            print(num[i][j], end='')
        print()
else:
    print('No')

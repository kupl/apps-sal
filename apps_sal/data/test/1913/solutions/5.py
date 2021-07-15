def good(s):
    counter = 0
    for i in s:
        if i == '1':
            counter += 1
        elif i != '0':
            return False
    return counter == 1

def count(s):
    ans = 0
    for i in s:
        if i == '0':
            ans += 1
    return ans


n = int(input())
d = input().split(' ')
if '0' in d:
    print('0')
    return
al = 0
ans = ''
for i in d:
    flag = good(i)
    if flag:
        al += count(i)
    else:
        ans = i
if ans == '':
    print('1' + al * '0')
else:
    print(ans + al * '0')


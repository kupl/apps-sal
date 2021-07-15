def get_down(i):
    if len(i) > 3 and i[-3] == '.':
        return int(i[-2:])
    return 0


def get_up(ans):
    if len(ans) > 3 and i[-3] == '.':
        ans = ans[:-3]
    ans = ans.replace('.', '')
    return int(ans)


def modify(up, down=0):
    ans = ''
    f = (up == 0)
    while up != 0:
        ans = str(up % 1000).rjust(3, '0') + '.' + ans
        up //= 1000
    ans = ans.lstrip('0')
    if down == 0:
        ans = ans[:-1]
    else:
        down = str(down).rjust(2, '0')
        ans += down
    if (f):
        ans = '0.' + ans
    return ans

s = input().strip()
numb = []
cur = ''
f = 0
for i in s:
    if '0' <= i <= '9':
        f = 1
        cur += i
    elif i == '.':
        cur += i
    elif 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        f = 0
        if (cur):
            numb.append(cur)
            cur = ''
if cur:
    numb.append(cur)
    cur = ''
ans_up = 0
ans_down = 0
for i in numb:
    #print(i, get_up(i), get_down(i))
    ans_up += get_up(i)
    ans_down += get_down(i)
ans_up += ans_down // 100
ans_down %= 100
print(modify(ans_up, ans_down))


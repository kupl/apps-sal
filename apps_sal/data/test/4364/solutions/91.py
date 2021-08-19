s = input()
b = int(s[:2])
a = int(s[2:])


def yorm(i):
    flag = 'none'
    if 0 < i <= 12:
        flag = 'MM'
    elif i < 100:
        flag = 'YY'
    return flag


bf = yorm(b)
af = yorm(a)
ans = bf + af
if len(ans) != 4:
    ans = 'NA'
if ans == 'MMMM':
    ans = 'AMBIGUOUS'
if ans == 'YYYY':
    ans = 'NA'
print(ans)

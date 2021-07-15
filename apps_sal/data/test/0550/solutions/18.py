def f(s):
    ans = ''
    for i in s:
        if i == 'l' or i == 'L' or i == 'i' or i == 'I':
            ans += '1'
        elif 'a' <= i <= 'z':
            ans += i.upper()
        elif i == '0':
            ans += 'O'
        else:
            ans += i
    return ans


s = input()
s = f(s)
n = int(input())
a = []
for i in range(n):
    ss = input()
    a.append(f(ss))
if s in a:
    print('No')
else:
    print('Yes')
#print(a)


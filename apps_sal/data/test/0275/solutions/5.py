def clean(d):
    ans = ['0']
    for c in list(d):
        ans.append(c)
        i = len(ans) - 1
        while i > 1 and ans[i - 2] == '0' and ans[i - 1] == '1' and ans[i] == '1':
            ans[i - 2] = '1'
            ans[i - 1] = '0'
            ans[i] = '0'
            i -= 2
    return ''.join(ans).lstrip('0')


a = clean(input())
b = clean(input())
if a == b:
    print('=')
elif len(a) > len(b):
    print('>')
elif len(a) < len(b):
    print('<')
elif a > b:
    print('>')
else:
    print('<')

def seq(s):
    ans = ''
    for i in s:
        if i != 'X':
            ans += i
    while ans[0] != 'A':
        ans = ans[1:] + ans[0]
    return ans


first = input() + input()[::-1]
second = input() + input()[::-1]
while first[0] != second[0]:
    first = first[1:] + first[0]
if seq(first) != seq(second):
    print('NO')
else:
    print('YES')

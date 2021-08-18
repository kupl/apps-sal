
n = int(input())
s = list(input())

cnt = s.count('x')
ans = cnt - n // 2
if ans > 0:
    tmp = ans
    for i, x in enumerate(s):
        if x == 'x':
            s[i] = 'X'
            tmp -= 1
            if tmp == 0:
                break
elif ans < 0:
    ans = -ans
    tmp = ans
    for i, x in enumerate(s):
        if x == 'X':
            s[i] = 'x'
            tmp -= 1
            if tmp == 0:
                break
print(ans)
print(''.join(s))

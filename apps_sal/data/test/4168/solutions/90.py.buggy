x = [0] * 32
x[0] = 1
x[1] = -2
for i in range(2, 32):
    x[i] = x[i - 2] + (-2)**i
n = int(input())
if n == 0:
    print(0)
    return
ans = ''
for i in range(2, 33)[::-1]:
    if i % 2:
        l = x[i - 2]
        r = x[i - 1]
    else:
        l = x[i - 1]
        r = x[i - 2]
    t = n - (-2)**i
    if l <= t and t <= r:
        n = t
        ans = ans + '1'
    else:
        ans = ans + '0'
ls = ['10', '11', '00', '01']
ans = ans + ls[n + 2]
for i in range(len(ans)):
    if ans[i] == '1':
        re = i
        break
print(ans[re:])

def check(ans, num, a, b, u):
    prob = ans
    a = []
    for i in range(len(num)):
        a.append(num[i])
    prob += num[u]
    a.pop(u)
    a.sort()
    for i in range(len(a)):
        prob += a[i]
    if int(prob) <= int(b):
        return True
    return False


a = input()
b = input()
num = []
ans = ''
if len(a) == len(b):
    for i in range(len(a)):
        num.append(a[i])
    num.sort()
    num.reverse()
    step = 0
    while num:
        for i in range(len(num)):
            if check(ans, num, a, b, i):
                ans += num[i]
                num.pop(i)
                break
    if num:
        ans += num[-1]
    print(ans)
else:
    num = []
    for i in range(len(a)):
        num.append(a[i])
    num.sort()
    num.reverse()
    ans = ''
    for i in range(len(num)):
        ans += num[i]
    print(ans)

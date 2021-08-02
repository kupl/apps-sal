def sk(k):
    tk = k
    ret = 0
    while tk != 0:
        ret += tk % 10
        tk //= 10
    return ret


ans = []
for i in range(1, 100):
    tmp = i / sk(i)
    if len(ans) == 0:
        ans.append((i, tmp))
    else:
        l = ans[-1]
        if l[1] > tmp:
            ans[-1] = (i, tmp)
        else:
            ans.append((i, tmp))

for j in range(15):
    for i in range(100, 1000):
        n = int(str(i) + ''.join(['9'] * j))
        tmp = n / sk(n)
        if ans[-1][1] > tmp:
            while ans[-1][1] > tmp:
                ans.pop()
        ans.append((n, tmp))

for i in range(int(input())):
    print(ans[i][0])

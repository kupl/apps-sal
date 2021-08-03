def run(a, ind, l):
    newSt = ''
    ans = 0
    for i in range(ind, len(a)):
        newSt += a[i]
        if int(newSt, 2) == (i - l + 1):
            ans += 1
        if int(newSt, 2) > (i - l + 1):
            return ans
    return ans


n = int(input())
for kkk in range(n):
    st = input()
    uk = [0] * len(st)
    for i in range(len(uk)):
        uk[i] = i

    for j in range(len(uk)):
        if st[j] == '1':
            uk[0] = j
            break
    for i in range(1, len(uk)):
        if i < uk[i - 1]:
            uk[i] = uk[i - 1]
        else:
            for j in range(i, len(uk)):
                if st[j] == '1':
                    uk[i] = j
                    break

    s = 0
    for i in range(len(uk)):
        if ((uk[i] != i) or st[i] == '1'):
            s += run(st, uk[i], i)
    print(s)

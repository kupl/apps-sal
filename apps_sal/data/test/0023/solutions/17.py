a = input().strip()
b = input().strip()
if len(b) > len(a):
    print(''.join(sorted(a))[::-1])
else:
    f = [0] * 11
    for ele in a:
        f[int(ele)] += 1
    ans = ''
    i = 0
    n = len(b)
    while i < n:
        num = int(b[i])
        if f[num]:
            ans += str(num)
            f[num] -= 1
        else:
            break
        i += 1

    flag = 0
    while True and len(ans) != len(a):
        num = int(b[i])
        num -= 1
        while num >= 0:
            if f[num]:
                ans += str(num)
                f[num] -= 1
                for j in range(9, -1, -1):
                    ans += (str(j) * f[j])
                break
            num -= 1
        if len(ans) == len(a):
            break
        f[int(ans[-1])] += 1
        ans = ans[:-1]
        i -= 1
    print(ans.strip())

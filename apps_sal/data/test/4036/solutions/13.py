n, k = list(map(int, input().split()))

mi = (k * (k + 1)) // 2
mx = 2**(k - 1)

if n < mi:
    print('NO')
else:
    ans = []
    for i in range(1, k + 1):
        ans.append(i)

    remain = n - mi

    add = remain // k
    if add:
        for i in range(k):
            ans[i] += add
        remain -= (k * add)

    while remain:
        i = k - 1
        while remain and ans[i] < (add + ans[0] * 2**(i)):
            ans[i] += 1
            i -= 1
            remain -= 1
        if ans[-1] == (add + ans[0] * 2**(k - 1)):
            break

    if remain:
        print('NO')
    else:
        print('YES')
        for a in ans[:-1]:
            print(a, end=" ")
        print(ans[-1])

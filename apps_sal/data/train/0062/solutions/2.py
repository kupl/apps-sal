for _ in range(int(input())):
    q = input()
    ans = q[0]
    test = [0] * 26
    j = 0
    c = 1
    for i in q[1:]:
        if j > 0 and ans[j - 1] == i:
            j -= 1
            continue
        if j < len(ans) - 1 and ans[j + 1] == i:
            j += 1
            continue
        if j == 0:
            ans = i + ans
            continue
        if j == len(ans) - 1:
            ans += i
            j += 1
            continue
        c = 0
    for i in ans:
        test[ord(i) - 97] += 1
    for i in range(26):
        if test[i] > 1:
            c = 0
        if test[i] == 0:
            ans += chr(i + 97)
    if c:
        print('YES')
        print(ans)
    else:
        print('NO')

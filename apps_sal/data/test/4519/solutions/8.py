q = int(input())
while q > 0:
    q -= 1
    (n, d) = list(map(int, input().split()))
    s = input()
    l = []
    for c in s:
        l.append(c)
    j = 0
    ans = ['' for i in range(n)]
    for i in range(n):
        if l[i] == '0':
            if i - j <= d:
                ans[j] = '0'
                l[i] = '*'
                d -= i - j
                j += 1
            else:
                ans[i - d] = '0'
                l[i] = '*'
                break
    i = 0
    index = 0
    while i < n:
        while l[index] == '*':
            index += 1
            if index >= n:
                break
        if index >= n:
            break
        if ans[i] == '':
            ans[i] = l[index]
            index += 1
        i += 1
    for k in ans:
        print(k, end='')
    print()
    print()

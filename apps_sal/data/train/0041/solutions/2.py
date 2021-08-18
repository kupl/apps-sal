for _ in range(int(input())):
    n, k = map(int, input().split())
    st = input()
    s = [st[i] for i in range(n)]
    res = '()' * (k - 1) + '(' * ((n - 2 * (k - 1)) // 2) + ')' * ((n - 2 * (k - 1)) // 2)
    ans = []
    for i in range(n):
        if s[i] != res[i]:
            for j in range(i + 1, n):
                if res[i] == s[j]:
                    ans.append([i + 1, j + 1])
                    sub = s[i:j + 1]
                    sub = sub[::-1]
                    for k in range(len(sub)):
                        s[i + k] = sub[k]
                    break
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

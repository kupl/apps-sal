for i in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    elems = [0 for i in range(2 * n + 1)]
    ans = []
    for i in range(len(s)):
        elems[s[i]] = 1
    for i in range(len(s)):
        ans.append(s[i])
        ch = s[i] + 1
        while ch <= 2 * n and elems[ch] != 0:
            ch += 1
        if ch > 2 * n:
            ans = -1
            break
        else:
            elems[ch] = 1
            ans.append(ch)
    if ans == -1:
        print(-1)
    else:
        print(*ans)

t = int(input())
while t:
    (n, m) = map(int, input().split())
    s = input()
    p = input().split()
    for i in range(m):
        p[i] = int(p[i])
    p.sort()
    ls = []
    count = 0
    for i in range(m):
        if i == 0:
            count += 1
            if i == m - 1:
                ls.append([p[i], count])
        elif p[i] == p[i - 1]:
            count += 1
            if i == m - 1:
                ls.append([p[i], count])
        else:
            ls.append([p[i - 1], count])
            count = 1
            if i == m - 1:
                ls.append([p[i], count])
    ls.append([n, 0])
    visited = [1 for i in range(n)]
    count = m
    j = 0
    for i in range(n):
        if i < ls[j][0]:
            visited[i] += count
        else:
            count -= ls[j][1]
            j += 1
            visited[i] += count
    ans = [0 for i in range(26)]
    for i in range(n):
        ans[ord(s[i]) - 97] += visited[i]
    print(*ans)
    t -= 1

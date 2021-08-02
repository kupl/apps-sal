for t in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())

    mk = 0
    for i in range(n):
        if s[i] == '1':
            for j in range(max(mk, i - k), min(i + k + 1, n)):
                s[j] = 'X'
            mk = j

    ans = 0
    newBoundary = -1
    for i in range(n):
        if i > newBoundary and s[i] == '0':
            ans += 1
            newBoundary = i + k
    print(ans)

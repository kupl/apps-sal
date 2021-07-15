for i in range(int(input())):
    n = int(input())
    s = input()
    ans = -1e9
    cur = 0
    fl = False
    for j in range(n):
        if s[j] == 'A':
            fl = True
            ans = max(ans, cur)
            cur = 0
        elif fl == True:
            cur += 1
    print(max(cur, ans))

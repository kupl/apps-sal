t = int(input())

for _ in range(t):
    n = int(input())
    r, p, s = map(int, input().split())
    S = input()
    ans = [None]*n
    win = 0
    for i, c in enumerate(S):
        if c == 'R' and p > 0:
            ans[i] = 'P'
            p -= 1
            win += 1
        elif c == 'P' and s > 0:
            ans[i] = 'S'
            s -= 1
            win += 1
        elif c == 'S' and r > 0:
            ans[i] = 'R'
            r -= 1
            win += 1
    for i in range(n):
        if ans[i] is None:
            if r > 0:
                ans[i] = 'R'
                r -= 1
            elif p > 0:
                ans[i] = 'P'
                p -= 1
            else:
                ans[i] = 'S'
                s -= 1

    if win >= (n+1)//2:
        print('YES')
        print(*ans, sep='')
    else:
        print('NO')

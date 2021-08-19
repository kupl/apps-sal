def d_menagerie():
    N = int(input())
    S = input()
    s = S + S[:2]
    for ans in ('SS', 'SW', 'WS', 'WW'):
        for i in range(1, N + 1):
            if ans[-1] == 'S' and s[i] == 'o' or (ans[-1] == 'W' and s[i] == 'x'):
                ans += ans[-2]
            else:
                ans += 'S' if ans[-2] == 'W' else 'W'
        if ans[:2] == ans[N:]:
            return ans[:N]
    return '-1'


print(d_menagerie())

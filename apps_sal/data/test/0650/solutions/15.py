def f(s):
    ok = set('AEFHIKLMNTVWXYZ')
    cnt = 0
    for i in s:
        if i in ok:
            cnt += 1
    return cnt == 0 or cnt == len(s)


print('YES' if f(input()) else 'NO')

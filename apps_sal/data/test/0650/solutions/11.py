(n, cnt) = (input(), 0)
for i in n:
    if i in set('AEFHIKLMNTVWXYZ'):
        cnt += 1
print('YES' if cnt == 0 or cnt == len(n) else 'NO')

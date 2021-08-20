s = input()
for x in s[::-1]:
    n = int(x)
    cur = ''
    if n >= 5:
        cur += '-O|'
        n -= 5
    else:
        cur += 'O-|'
    cur += ''.join(['O' for j in range(n)]) + '-' + ''.join(['O' for j in range(4 - n)])
    print(cur)

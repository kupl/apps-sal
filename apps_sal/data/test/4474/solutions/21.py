q = int(input())


def dec_to_base(N, base):
    if not hasattr(dec_to_base, 'table'):
        dec_to_base.table = '0123456789ABCDEF'
    (x, y) = divmod(N, base)
    return dec_to_base(x, base) + dec_to_base.table[y] if x else dec_to_base.table[y]


for i in range(q):
    n = int(input())
    s = list(str(dec_to_base(n, 3)))
    balance = n
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '2':
            balance -= 3 ** (len(s) - i - 1)
            s[i] = '1'
    for i in range(len(s) - 1, -1, -1):
        if balance >= n:
            break
        if s[i] == '0' and balance < n:
            s[i] = '1'
            balance += 3 ** (len(s) - i - 1)
    while balance < n:
        balance *= 3
        s.append('0')
        if balance < n:
            s[-1] = '1'
            balance += 1
        else:
            break
    for i in range(len(s)):
        if balance - 3 ** (len(s) - i - 1) >= n:
            balance -= 3 ** (len(s) - i - 1)
            s[i] = '0'
    print(int(''.join(s), 3))

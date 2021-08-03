n = input()
i = 0
k = len(n) - 1
_b = True
while i <= k and _b:
    if n[i] == n[k] and n[i] in ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y']:
        _b = True
        i += 1
        k -= 1
    else:
        _b = False
if _b:
    print('YES')
else:
    print('NO')

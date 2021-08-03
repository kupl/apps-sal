def go():
    s = input()
    p = s.count('o')
    l = s.count('-')

    if p == 0:
        return 'YES'
    if l % p == 0:
        return 'YES'
    return 'NO'


print(go())

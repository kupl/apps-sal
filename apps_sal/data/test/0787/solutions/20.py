k, q, v, s = int(input()), input(), 'YES', set()
for ch in q:
    if k == 0 or ch in s:
        v += ch
    else:
        v += '\n' + ch
        s.add(ch)
        k -= 1
print('NO' if k else v)

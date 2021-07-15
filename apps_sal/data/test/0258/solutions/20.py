def winner(s, n):
    s1 = s[:n//2]
    s2 = s[n//2:]
    turns = s.count('?') // 2
    l1 = r1 = l2 = r2 = 0
    for c in s1:
        if c == '?':
            r1 += 9
        else:
            l1 += int(c)
            r1 += int(c)
    for c in s2:
        if c == '?':
            r2 += 9
        else:
            l2 += int(c)
            r2 += int(c)
    if r1 < l2 or r2 < l1:
        return 'True'
    minDif = min(r1 - l2, r2 - l1)
    return minDif < turns * 9


n = int(input())
s = input()
print('Monocarp' if winner(s, n) else 'Bicarp')


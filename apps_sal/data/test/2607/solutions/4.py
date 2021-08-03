t = int(input())
letters = ['a', 'b', 'c']
for iTest in range(t):
    s = list(input())
    valid = True
    prev = ''
    for c in s:
        if c == prev and c != '?':
            valid = False
            break
        prev = c
    if not valid:
        print(-1)
        continue
    for i in range(len(s)):
        if s[i] != '?':
            continue
        ns = set()
        if i > 0:
            ns.add(s[i - 1])
        if i < len(s) - 1:
            ns.add(s[i + 1])
        for l in letters:
            if l not in ns:
                s[i] = l
                break
    print("".join(s))

s = input()
while s:
    m = [t for t in ['dream', 'dreamer', 'erase', 'eraser'] if s.endswith(t)]
    if not m:
        print('NO')
        return
    s = s[:-len(m[0])]
print('YES')

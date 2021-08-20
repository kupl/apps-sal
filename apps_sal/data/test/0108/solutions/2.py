s = list(input())
st = 'a'
for i in range(len(s)):
    if s[i] <= st:
        s[i] = st
        st = chr(ord(st) + 1)
    if st > 'z':
        break
if st <= 'z':
    print(-1)
else:
    print(*s, sep='')

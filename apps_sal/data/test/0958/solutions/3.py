n, size = map(int, input().split())
s = input()
ans = []
for f in s:
    if ord(f) - ord('a') > ord('z') - ord(f) and ord(f) - ord('a') < size:
        ans.append('a')
        size -= (ord(f) - ord('a'))
    elif ord('z') - ord(f) > ord(f) - ord('a') and ord('z') - ord(f) < size:
        ans.append('z')
        size -= ord('z') - ord(f)
    elif ord(f) - ord('a') >= size:
        ans.append(chr(ord(f) - size))
        size = 0
        break
    else:
        ans.append(chr(ord(f) + size))
        size = 0
        break
if size:
    print('-1')
else:
    ans.extend(s[len(ans):])
    print(''.join(ans))

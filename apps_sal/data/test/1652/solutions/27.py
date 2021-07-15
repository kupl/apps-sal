daydream = ['dream', 'dreamer', 'erase', 'eraser']
s = input()
import sys
while s:
    for i in daydream:
        if s.endswith(i):
            s = s[:-len(i)]
            break
    else:
        break
else:
    print('YES')
    return
print('NO')

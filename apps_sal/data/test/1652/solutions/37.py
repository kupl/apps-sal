S = input()
rS = S[::-1]
keys = ['dream', 'dreamer', 'erase', 'eraser']
reversed_keys = [keys[i][::-1] for i in range(len(keys))]
i = 0

while i < len(rS):
    if rS[i:i+5] in reversed_keys:
        i += 5
    elif rS[i:i+6] in reversed_keys:
        i += 6
    elif rS[i:i+7] in reversed_keys:
        i += 7
    else:
        break
if i == len(rS):
    print('YES')
else:
    print('NO')


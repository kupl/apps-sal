z = input()
l = []
for x in z:
    if ord(x) >= ord('0') and ord(x) <= ord('9'):
        l.append(ord(x) - ord('0'))
    elif ord(x) >= ord('A') and ord(x) <= ord('Z'):
        l.append(ord(x) - ord('A') + 10)
    elif ord(x) >= ord('a') and ord(x) <= ord('z'):
        l.append(ord(x) - ord('a') + 36)
    elif ord(x) == ord('-'):
        l.append(62)
    else:
        l.append(63)
ans = 1
for i in l:
    unset = 6 - bin(i).count('1')
    for x in range(unset):
        ans *= 3
        while ans >= 1000000007:
            ans -= 1000000007
print(ans)

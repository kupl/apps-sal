s = input()
a = [int(i) for i in '0' * 26]
k = -1
for i in s:
    a[ord(i) - 97] += 1
for i in range(25):
    if a[i] % 2 != 0:
        for j in range(25 - i):
            if a[25 - j] % 2 != 0:
                a[i] += 1
                a[25 - j] -= 1
                break
    if a[i] % 2 != 0:
        k = i
        break
st = ''
for i in range(26):
    if a[i] > 0:
        st += chr(i + 97) * (a[i] // 2)
if k != -1:
    st = st + chr(k + 97) + st[::-1]
else:
    st = st + st[::-1]
print(st)

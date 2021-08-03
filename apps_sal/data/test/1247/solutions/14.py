s = input()
a = [0] * 26
for c in s:
    a[ord(c) - ord('a')] += 1

cnt = 0
for i in range(26):
    if a[i] % 2 == 1:
        cnt += 1

if cnt == 0:
    print('First')
elif cnt % 2 == 0:
    print('Second')
else:
    print('First')

n = int(input())
s = input()
(r, delta) = (0, 0)
for i in range(n // 2):
    if s[i] == '?':
        r += 1
    else:
        delta += int(s[i])
for i in range(n // 2, n):
    if s[i] == '?':
        r -= 1
    else:
        delta -= int(s[i])
if r < 0:
    r = -r
    delta = -delta
if delta + 9 * r // 2 == 0:
    print('Bicarp')
else:
    print('Monocarp')

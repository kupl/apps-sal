s = input()
n = len(s)
for i in range(n):
    if s[i] == '^':
        x = i
        break
a = b = 0
for i in range(x):
    if s[i] >= '1' and s[i] <= '9':
        a += (int(s[i]) - int('0')) * (x - i)
for i in range(x, n):
    if s[i] >= '1' and s[i] <= '9':
        b += (int(s[i]) - int('0')) * (i - x)
if a == b:
    print('balance')
else:
    print('left' if a > b else 'right')

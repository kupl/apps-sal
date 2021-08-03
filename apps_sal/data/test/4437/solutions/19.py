n = int(input())
s = [i for i in input()]
temp = ''
ans = 0
for i, j in enumerate(s):
    if i % 2:
        if temp == 'a':
            if j == 'a':
                ans += 1
            s[i] = 'b'
        else:
            if j == 'b':
                ans += 1
            s[i] = 'a'
    else:
        temp = j
print(ans)
print(''.join(s))

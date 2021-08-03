n = int(input())
s = input()
d = ''
d = s[0:2]
count = 0
i = 1
while i < n:
    if s[i] + s[i - 1] == 'RU' or s[i] + s[i - 1] == 'UR':
        count += 1
        i += 2
    else:
        i += 1
print(n - count)

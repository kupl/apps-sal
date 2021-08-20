n = int(input())
s = list(input())
pref = [0]
k = 0
for i in range(0, n - 1, 2):
    if s[i] == s[i + 1]:
        k += 1
        if s[i] == 'b':
            s[i] = 'a'
        else:
            s[i] = 'b'
print(k)
print(''.join(s))

s1 = input()
s = ''
for i in s1:
    if i in 'ab':
        s += i
n = len(s)
ans = 1
i = 0
while i < n:
    x = 0
    while i < n and s[i] == 'a':
        i += 1
        x += 1
    ans *= x + 1
    i += 1
MOD = 10 ** 9 + 7
print((ans - 1) % MOD)

n = input()
s = input()
answ = 0
k = 0
for i in range(len(s)):
    if s[i] == 'B':
        answ += 2 ** i
print(answ)

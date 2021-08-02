n = input()
s = ''
for i in n:
    if i == '7':
        s = s + '1'
    else:
        s = s + '0'
ans = 0
for i in range(len(n) - 1):
    ans += 2**(i + 1)
print(ans + int(s, 2) + 1)

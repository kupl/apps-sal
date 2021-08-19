n = int(input())
c = 0
s = input()
ans = ''
ans_n = 0
for i in range(n):
    if s[i] == 'B':
        c += 1
    else:
        if c != 0:
            ans += str(c) + ' '
            ans_n += 1
        c = 0
if c != 0:
    ans += str(c) + ' '
    ans_n += 1
print(ans_n)
print(ans)

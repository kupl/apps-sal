N = int(input())
s = input()

keep = 0
ans = ''
for i in range(N):
    if s[i] == '(':
        ans += '('
        keep += 1
    else:
        if keep > 0:
            ans += ')'
            keep -= 1
        else:
            ans = ('(' + ans + ')')
print((ans + ')' * keep))


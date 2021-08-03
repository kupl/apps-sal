n = int(input())
s = input()
cnt, L = 0, 0
for i in range(len(s)):
    if s[i] == '(':
        cnt += 1
    else:
        cnt -= 1

    if cnt < 0:
        L = min(L, cnt)

ans = '(' * abs(L) + s
R = ans.count('(') - ans.count(')')
ans += ')' * R

print(ans)

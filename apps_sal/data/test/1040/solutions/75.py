n = int(input())
s = input()

ans = ''

for i in range(n):
    ans += s[i]
    if len(ans) < 3: continue
    if ans[-3:] == 'fox':
        ans = ans[:-3]
print(len(ans))

n = int(input())
s = input()
ans = ''
for i in s:
    ans += i
    if ans[-3:] == 'fox':
        ans = ans[:-3]
print(len(ans))

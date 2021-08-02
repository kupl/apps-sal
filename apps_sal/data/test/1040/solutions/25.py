n = int(input())
s = list(input())
ans = []
for c in s:
    ans.append(c)
    if ''.join(ans[-3:]) == 'fox':
        ans.pop()
        ans.pop()
        ans.pop()
print(len(ans))

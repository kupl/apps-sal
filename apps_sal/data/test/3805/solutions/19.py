ans = []
for c in input():
    if len(ans) and ans[-1] == c:
        ans.pop()
    else:
        ans += [c]
print('No' if len(ans) else 'Yes')

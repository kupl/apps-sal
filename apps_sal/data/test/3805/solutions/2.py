s = input()
ans = [0] * len(s)
n = 0
for x in s:
    if n and ans[n - 1] == x:
        n -= 1
    else:
        ans[n] = x
        n += 1
print('No' if n else 'Yes')

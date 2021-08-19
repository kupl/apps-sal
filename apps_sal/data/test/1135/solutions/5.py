n = int(input())
s = input()
s = s[::-1]
f = True
ans = []
for i in s:
    if f:
        ans.insert((len(ans) + 1) // 2, i)
        f = False
    else:
        ans.insert(len(ans) // 2, i)
        f = True
print(''.join((str(i) for i in ans)))

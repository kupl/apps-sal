n = int(input())
ans = ['Power', 'Time', 'Space', 'Soul', 'Reality', 'Mind']
for i in range(n):
    s = input()
    if s == 'purple':
        del ans[ans.index('Power')]
    elif s == 'green':
        del ans[ans.index('Time')]
    elif s == 'blue':
        del ans[ans.index('Space')]
    elif s == 'orange':
        del ans[ans.index('Soul')]
    elif s == 'red':
        del ans[ans.index('Reality')]
    else:
        del ans[ans.index('Mind')]
print(len(ans))
for a in ans:
    print(a)

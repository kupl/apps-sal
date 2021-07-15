ans = []
for _ in range(int(input())):
    u = list(map(int, list(input())))
    a1 = sum(u)
    a0 = len(u) - a1
    d = min(a0, a1)
    if d % 2 == 1:
        ans.append('DA')
    else:
        ans.append('NET')
print('\n'.join(ans))


ans = []
for _ in range(int(input())):
    n = int(input())
    u = list(map(int, list(input())))
    for i in range(n):
        if u[i] == 1:
            i1 = i
            break
    else:
        ans.append(''.join(map(str, u)))
        continue
    for i in range(n - 1, -1, -1):
        if u[i] == 0:
            i2 = i
            break
    else:
        ans.append(''.join(map(str, u)))
        continue
    if i2 < i1:
        ans.append(''.join(map(str, u)))
        continue
    u1 = '0' * i1 + '0' + '1' * (n - i2 - 1)
    ans.append(u1)
print('\n'.join(ans))

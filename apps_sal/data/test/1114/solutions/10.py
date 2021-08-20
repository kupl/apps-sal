(n, m) = map(int, input().split())
f = list(map(int, input().split()))
b = list(map(int, input().split()))
f_count = [0 for i in range(n + 1)]
f_pos = [0 for i in range(n + 1)]
for i in range(n):
    f_pos[f[i]] = i + 1
    f_count[f[i]] += 1
ans = []
Ambiguity = False
Impossible = False
for i in range(m):
    if f_count[b[i]] == 1:
        ans.append(f_pos[b[i]])
    elif f_count[b[i]] == 0:
        Impossible = True
        break
    else:
        Ambiguity = True
if Impossible:
    print('Impossible')
elif Ambiguity:
    print('Ambiguity')
else:
    print('Possible')
    print(*ans)

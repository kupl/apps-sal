h, w = list(map(int, input().split()))

ans = 'Yes'

s = []
for i in range(h):
    s += input().split()


s.insert(0, ''.join(['.'] * (w + 2)))
s = list(map(lambda x: '.' + x + '.', s))
s.insert(len(s), ''.join(['.'] * (w + 2)))

s = list(map(list, s))

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if (s[i][j] == '
            ans='No'
            break
    else:
        continue
    break

print(ans)

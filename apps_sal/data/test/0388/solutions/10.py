n, k = map(int, input().split())
l = [True if x == 'YES' else False for x in input().split()]

res = list(range(k - 1))
for i in l:
    if i:
        for j in range(k):
            if j not in res[-k + 1:]:
                res.append(j)
                break
    else:
        res.append(res[-k + 1])

names = [chr(x) + chr(y) for x in range(ord('A'), ord('Z') + 1) for y in range(ord('a'), ord('z') + 1)]

for i in res:
    print(names[i], end=' ')
print()

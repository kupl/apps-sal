(n, k) = list(map(int, input().split()))
s = list(map(int, input().split()))
a = set()
x = 0
sol = []
for i in range(n):
    if s[i] not in a and x < k:
        a.add(s[i])
        x += 1
        sol.append(i + 1)
    if x == k:
        break
if x == k:
    print('YES')
    for i in sol:
        print(i, end=' ')
else:
    print('NO')

d = []
for _ in range(int(input())):
    d.append(input())

d.sort(key = len)

for i in range(len(d) - 1, 0, -1):
    c, p = d[i], d[i-1]
    if p not in c:
        print('NO')
        return

print("YES")
print(*d, sep = '\n')


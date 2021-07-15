n = int(input())
b = list(map(int, input().split()))
c = [0] * 1010

for i in range(len(b)):
    c[b[i]] = 1
for i in range(1, 999):
    if c[i] and c[i + 1] and c[i + 2]:
        print('YES')
        return
print('NO')

n = int(input())
p = list(map(int, input().split()))
error = 0
for i in range(n):
    if p[i] != i + 1:
        error += 1
    if error > 2:
        print('NO')
        return
print('YES')

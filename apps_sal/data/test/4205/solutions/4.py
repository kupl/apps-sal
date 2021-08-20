n = int(input())
p = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if p[i] == i + 1:
        continue
    p[p[i] - 1] = p[i]
    p[i] = i + 1
    cnt += 1
print('YES' if cnt <= 1 else 'NO')

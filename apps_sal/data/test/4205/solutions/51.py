n = int(input())
p = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if p[i] != i + 1:
        cnt += 1
print('YES' if cnt == 0 or cnt == 2 else 'NO')

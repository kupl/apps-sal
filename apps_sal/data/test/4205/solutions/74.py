n = int(input())
c = list(range(1, n + 1))
p = list(map(int, input().split()))
cnt = 0
for i in range(n):
    cnt += 1 if c[i] != p[i] else 0
print('YES' if cnt == 2 or cnt == 0 else 'NO')

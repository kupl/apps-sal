n = int(input())
C = list((i for i in range(1, n + 1)))
L = list(map(int, input().split()))
cnt = 0
for (c, l) in zip(C, L):
    if c != l:
        cnt += 1
print('YES' if cnt == 0 or cnt == 2 else 'NO')

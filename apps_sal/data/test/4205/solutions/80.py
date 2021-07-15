N = int(input())
P = list(map(int, input().split()))

cnt = 0

for i in range(N):
    if i+1 != P[i]:
        cnt += 1
    if cnt > 2:
        print('NO')
        return

print('YES')

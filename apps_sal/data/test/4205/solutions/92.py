n = int(input())
A = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if A[i] != i + 1:
        cnt += 1
if cnt <= 2:
    print('YES')
else:
    print('NO')

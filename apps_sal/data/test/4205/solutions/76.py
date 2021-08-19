N = int(input())
lst = list(map(int, input().split()))
k = 0
for i in range(N):
    if i + 1 != lst[i]:
        k += 1
if k <= 2:
    print('YES')
else:
    print('NO')

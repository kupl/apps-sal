N = int(input())
pi = list(map(int, input().split()))
count = 0
for i in range(N):
    if pi[i] != i + 1:
        count += 1
if count == 0 or count == 2:
    print('YES')
else:
    print('NO')

N = int(input())
p = list(map(int, input().split()))
check = 0
for i in range(N):
    if i + 1 != p[i]:
        check += 1
print('YES' if check <= 2 else 'NO')

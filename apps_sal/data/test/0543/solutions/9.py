n = int(input())
a = list(map(int, input().split()))
a.append(0)
for i in range(n+1):
    if a[i] < 0:
        print('NO')
        return
    a[i] %= 2
    if a[i] == 1:
        a[i+1] -= 1
print('YES')


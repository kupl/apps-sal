n = int(input())
l = list(map(int, input().split()))
for i in range(n):
    if l[i] == l[l[l[l[i] - 1] - 1] - 1]:
        print('YES')
        n = -1
        break
if n != -1:
    print('NO')

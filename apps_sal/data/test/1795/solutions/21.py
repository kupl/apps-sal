n = int(input())
l = list(map(int, input().split()))

flag = False
for i in range(n):
    if l[l[l[i] - 1] - 1] == i + 1:
        print('YES')
        flag = True
        break

if not flag:
    print('NO')


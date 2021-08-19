n = int(input())
s = []
for i in range(n):
    s.append([i for i in input().split()])
for i in s:
    if int(i[1]) >= 2400 and int(i[2]) > int(i[1]):
        print('YES')
        break
else:
    print('NO')

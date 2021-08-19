n = int(input())
list = []
for i in range(n):
    (a, b) = input().split()
    list.append([float(a), b])
ans = 0
for i in range(n):
    if list[i][1] == 'JPY':
        ans += list[i][0]
    else:
        ans += 380000 * list[i][0]
print(ans)

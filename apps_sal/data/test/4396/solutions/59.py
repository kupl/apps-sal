n = int(input())
li = [list(input().split()) for i in range(n)]
total = 0
for i in range(n):
    if li[i][1] == 'JPY':
        total += float(li[i][0])
    else:
        total += float(li[i][0]) * 380000.0
print(total)

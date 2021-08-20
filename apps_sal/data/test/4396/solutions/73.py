n = int(input())
num = 0
for i in range(n):
    (x1, v1) = map(str, input().split())
    if v1 == 'JPY':
        num += int(x1)
    else:
        num += float(x1) * 380000
print(num)

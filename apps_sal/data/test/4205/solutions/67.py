b = int(input())
a = list(map(int,input().split()))
count = 0
for i in range(b):
    if a[i] != i + 1 :
        count += 1
if count <= 2:
    print('YES')
else:
    print('NO')

n = int(input())
k = 0
for i in range(n):
    a, b = map(int, input().split())
    if a != b:
        k = 1
if k == 0:
    print('Poor Alex')
else:
    print('Happy Alex')

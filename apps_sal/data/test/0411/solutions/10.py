a, b = list(map(int, input().split()))
for i in range(a + b):
    n, m = list(map(int, input().split()))
if a == b:
    print('Yes')
else:
    print('No')

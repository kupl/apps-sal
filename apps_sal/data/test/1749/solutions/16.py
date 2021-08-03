A = list(map(int, input().split()))
n = A[0]
l = A[1]
r = A[2]
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 1
for i in range(0, l - 1):
    if a[i] != b[i]:
        ans = 0
for i in range(r, n):
    if a[i] != b[i]:
        ans = 0
if ans == 0:
    print('LIE')
else:
    print('TRUTH')

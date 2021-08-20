K = int(input())
(A, B) = map(int, input().split())
n = 0
for i in range(A, B + 1):
    if i % K == 0:
        n = 1
        break
if n == 1:
    print('OK')
else:
    print('NG')

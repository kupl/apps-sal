N = int(input())
n = [int(input())for i in range(N)]
s = sum(n)
w = 0
for k in range(2**N):
    p = sum(n[i]for i in range(N)if k & (1 << i))
    if (s - p - p) % 360 == 0:
        print('YES')
        w = 1
        break
if w == 0:
    print('NO')

import math
n, m = map(int, input().split())
if m > n * (n - 1) // 2 or m < n - 1:
    print("Impossible");return

rm = m - (n - 1)
ans = [(0, 0)] * (rm * 10)
f = 0

for i in range(3, n+1):
    for j in range(1, i-1):
        if not rm:
            break
        if math.gcd(j, i) == 1:
            ans[f] = (j, i)
            f += 1
            rm -= 1

if rm:
    print('Impossible');return

print('Possible')
for i in range(1, n):
    print(i, i+1)

for i in range(f):
    print(ans[i][0], ans[i][1])

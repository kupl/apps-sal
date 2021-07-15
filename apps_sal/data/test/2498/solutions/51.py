import math
N, M = map(int, input().split())
B = tuple(int(a) // 2 for a in input().split())

x = B[0]
for i in range(1, N):
    x = (x * B[i]) // math.gcd(x, B[i])

for b in B:
    if (x // b) % 2 == 0:
        print(0)
        break
else:
    ans = (M // x) - (M // (2 * x))
    print(ans)

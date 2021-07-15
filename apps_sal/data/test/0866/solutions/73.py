kMod = 1000000007

X, Y = map(int, input().split())

if (X+Y) % 3 != 0:
    print(0)
    return

offset = (X+Y)//3
X, Y = X-offset, Y-offset
if X < 0 or Y < 0:
    print(0)
    return

X, Y = max(X, Y), min(X, Y)

ans = 1
for i in range(X+1, X+Y+1):
    ans *= i
    ans %= kMod

for i in range(2, Y+1):
    ans *= pow(i, kMod-2, kMod)
    ans %= kMod

print(ans)

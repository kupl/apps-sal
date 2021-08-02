import sys
input = sys.stdin.readline

X, Y = list(map(int, input().split()))
ans = 0
for i in range(100):
    temp = X * (2**i)
    if temp > Y:
        ans = i
        break
print(ans)

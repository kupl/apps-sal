import sys
input = sys.stdin.readline
N = int(input())
L = list(map(int, input().split()))
t = 0
ans = 0
l = 0
r = 0
while r <= N - 1:
    if t + L[r] == t ^ L[r]:
        t += L[r]
        r += 1
    else:
        ans += r - l
        t -= L[l]
        l += 1
ans += (r - l) * (r - l + 1) / 2
print(int(ans))

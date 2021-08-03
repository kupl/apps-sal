N = int(input())
H = [int(i) for i in input().split()]
ans = 0
s = 0

for i in range(1, N):
    if H[i - 1] >= H[i]:
        s += 1
    else:
        t = max(ans, s)
        ans = t
        s = 0

t = max(ans, s)
ans = t
print(ans)
